#!/usr/bin/env python3
"""
Claude Code Documentation Reviewer
Automated documentation review following Google Developer Documentation Style Guide
"""

import os
import sys
import json
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
import anthropic
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GoogleStyleGuide:
    """Google Developer Documentation Style Guide rules and checks"""
    
    RULES = {
        # Writing style rules
        'active_voice': {
            'description': 'Use active voice instead of passive voice',
            'examples': ['Use "Configure the API" instead of "The API should be configured"']
        },
        'second_person': {
            'description': 'Use second person (you/your) to address the reader',
            'examples': ['Use "you can configure" instead of "one can configure"']
        },
        'present_tense': {
            'description': 'Use present tense for instructions',
            'examples': ['Use "Click Save" instead of "You will click Save"']
        },
        'clear_headings': {
            'description': 'Use clear, descriptive headings that tell users what they\'ll accomplish',
            'examples': ['Use "Configure SSL certificates" instead of "SSL"']
        },
        'parallel_structure': {
            'description': 'Use parallel structure in lists and procedures',
            'examples': ['All list items should start with the same part of speech']
        },
        'concise_language': {
            'description': 'Use concise, clear language. Avoid unnecessary words',
            'examples': ['Use "To configure" instead of "In order to configure"']
        },
        
        # Technical writing rules
        'numbered_procedures': {
            'description': 'Use numbered lists for sequential procedures',
            'examples': ['Step-by-step instructions should be numbered']
        },
        'code_formatting': {
            'description': 'Use proper code formatting and syntax highlighting',
            'examples': ['Code blocks should specify language for syntax highlighting']
        },
        'link_text': {
            'description': 'Use descriptive link text, avoid "click here" or "read more"',
            'examples': ['Use "View the API documentation" instead of "click here"']
        },
        'consistent_terminology': {
            'description': 'Use consistent terminology throughout the documentation',
            'examples': ['Don\'t mix "repository" and "repo" in the same document']
        },
        
        # Structure rules
        'logical_flow': {
            'description': 'Structure content in logical order: overview, prerequisites, procedures, troubleshooting',
            'examples': ['Start with what users will accomplish, then provide steps']
        },
        'scannable_content': {
            'description': 'Make content scannable with headings, lists, and short paragraphs',
            'examples': ['Break up long paragraphs, use subheadings']
        }
    }
    
    @classmethod
    def get_review_prompt(cls, content: str, filename: str) -> str:
        """Generate a comprehensive review prompt for Claude"""
        rules_text = "\n".join([
            f"- **{rule}**: {details['description']}\n  Examples: {'; '.join(details['examples'])}"
            for rule, details in cls.RULES.items()
        ])
        
        return f"""You are an expert technical writer reviewing documentation for adherence to the Google Developer Documentation Style Guide. 

Please review the following documentation file: `{filename}`

**Content to review:**
```markdown
{content}
```

**Google Developer Style Guide Rules to check:**
{rules_text}

**Review Instructions:**
1. Analyze the content for adherence to Google Developer Documentation Style Guide
2. Identify specific issues with line numbers when possible
3. Provide actionable suggestions for improvement
4. Focus on the most impactful changes that improve clarity and usability
5. Consider the target audience (technical writers and developers)
6. Check for proper markdown formatting and structure

**Output Format:**
Provide your review in the following JSON format:
```json
{{
  "overall_score": "good|needs_improvement|poor",
  "summary": "Brief overall assessment",
  "issues": [
    {{
      "type": "style|structure|formatting|terminology",
      "severity": "high|medium|low", 
      "line": "line number if applicable",
      "issue": "Description of the issue",
      "suggestion": "Specific improvement suggestion",
      "example": "Example of improved text if applicable"
    }}
  ],
  "positive_aspects": ["List of things done well"],
  "recommendations": ["List of key recommendations for improvement"]
}}
```

Focus on providing practical, actionable feedback that will help improve the documentation quality."""

class ClaudeDocsReviewer:
    """Main class for Claude-powered documentation review"""
    
    def __init__(self):
        # Check if we're using company LiteLLM proxy
        self.litellm_base_url = os.getenv('LITELLM_BASE_URL')
        self.litellm_api_key = os.getenv('LITELLM_API_KEY')
        
        if self.litellm_base_url and self.litellm_api_key:
            # Use company LiteLLM proxy with direct HTTP requests
            logger.info(f"Using LiteLLM proxy at: {self.litellm_base_url}")
            self.use_litellm = True
            self.client = None  # Will use direct HTTP for LiteLLM
        else:
            # Fall back to direct Anthropic API
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                raise ValueError("Either LITELLM_API_KEY+LITELLM_BASE_URL or ANTHROPIC_API_KEY must be set")
            logger.info("Using direct Anthropic API")
            self.use_litellm = False
            self.client = anthropic.Anthropic(api_key=api_key)
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.repo_owner = os.getenv('REPO_OWNER')
        self.repo_name = os.getenv('REPO_NAME')
        self.pr_number = os.getenv('PR_NUMBER')
        
        if not all([self.client.api_key, self.github_token, self.repo_owner, self.repo_name]):
            raise ValueError("Missing required environment variables")
    
    def get_file_content(self, file_path: str, sha: str) -> Optional[str]:
        """Get file content from GitHub at specific commit"""
        try:
            url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contents/{file_path}"
            headers = {'Authorization': f'token {self.github_token}'}
            params = {'ref': sha}
            
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                import base64
                content = response.json()['content']
                return base64.b64decode(content).decode('utf-8')
            return None
        except Exception as e:
            logger.error(f"Error getting file content for {file_path}: {e}")
            return None
    
    def call_claude_api(self, prompt: str) -> str:
        """Call Claude API - either through LiteLLM proxy or direct Anthropic API"""
        if self.use_litellm:
            return self._call_litellm_proxy(prompt)
        else:
            return self._call_anthropic_direct(prompt)
    
    def _call_litellm_proxy(self, prompt: str) -> str:
        """Call Claude through company LiteLLM proxy"""
        import requests
        
        url = f"{self.litellm_base_url.rstrip('/')}/v1/chat/completions"
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.litellm_api_key}',  # Standard Bearer token
            'x-api-key': self.litellm_api_key,  # Standard Anthropic header
            'x-litellm-api-key': self.litellm_api_key  # LiteLLM specific header
        }
        
        data = {
            'model': 'claude-3-sonnet-20240229',  # Use more widely supported model name
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 4000,
            'temperature': 0.1
        }
        
        logger.info(f"Making LiteLLM request to: {url}")
        logger.info(f"Using model: {data['model']}")
        logger.info(f"Request headers: {dict(headers)}")
        
        try:
            response = requests.post(url, headers=headers, json=data, timeout=120)
            
            logger.info(f"Response status code: {response.status_code}")
            logger.info(f"Response headers: {dict(response.headers)}")
            
            if response.status_code != 200:
                logger.error(f"LiteLLM API error: {response.status_code}")
                logger.error(f"Response text: {response.text}")
                raise Exception(f"Error code: {response.status_code} - {response.json() if response.text else 'No response body'}")
            
            result = response.json()
            
            if 'choices' not in result or not result['choices']:
                logger.error(f"Unexpected response format: {result}")
                raise Exception(f"Unexpected response format: {result}")
                
            content = result['choices'][0]['message']['content']
            logger.info(f"Successfully received response of length: {len(content)}")
            return content
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request exception: {e}")
            raise Exception(f"Request failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error in LiteLLM call: {e}")
            raise
    
    def _call_anthropic_direct(self, prompt: str) -> str:
        """Call Claude through direct Anthropic API"""
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",  # Keep newer model for direct API
            max_tokens=4000,
            temperature=0.1,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

    def review_file(self, file_path: str, content: str) -> Dict[str, Any]:
        """Review a single file using Claude"""
        try:
            prompt = GoogleStyleGuide.get_review_prompt(content, file_path)
            
            # Call Claude API (either LiteLLM or direct)
            response_text = self.call_claude_api(prompt)
            
            # Extract JSON from response
            start_marker = "```json"
            end_marker = "```"
            
            if start_marker in response_text:
                json_start = response_text.find(start_marker) + len(start_marker)
                json_end = response_text.find(end_marker, json_start)
                json_str = response_text[json_start:json_end].strip()
            else:
                # Fallback: try to parse the entire response as JSON
                json_str = response_text.strip()
            
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                logger.warning(f"Could not parse JSON response for {file_path}")
                return {
                    "overall_score": "needs_improvement",
                    "summary": "Review completed but response format needs adjustment",
                    "issues": [],
                    "positive_aspects": [],
                    "recommendations": ["Re-run review with updated prompt"]
                }
                
        except Exception as e:
            logger.error(f"Error reviewing file {file_path}: {e}")
            return {
                "overall_score": "error", 
                "summary": f"Review failed: {str(e)}",
                "issues": [],
                "positive_aspects": [],
                "recommendations": []
            }
    
    def format_review_comment(self, reviews: Dict[str, Dict[str, Any]]) -> str:
        """Format review results into a GitHub comment"""
        if not reviews:
            return "🤖 **Claude Code Documentation Review**\n\nNo documentation files found to review."
        
        comment_parts = [
            "🤖 **Claude Code Documentation Review**",
            "*Automated review following Google Developer Documentation Style Guide*",
            ""
        ]
        
        # Summary statistics
        total_files = len(reviews)
        good_files = sum(1 for r in reviews.values() if r.get('overall_score') == 'good')
        needs_improvement = sum(1 for r in reviews.values() if r.get('overall_score') == 'needs_improvement')
        poor_files = sum(1 for r in reviews.values() if r.get('overall_score') == 'poor')
        
        comment_parts.extend([
            f"## 📊 Review Summary",
            f"- **Files reviewed:** {total_files}",
            f"- **Good:** {good_files} 📗",
            f"- **Needs improvement:** {needs_improvement} 📙", 
            f"- **Poor:** {poor_files} 📕",
            ""
        ])
        
        # Individual file reviews
        for file_path, review in reviews.items():
            score_emoji = {
                'good': '✅', 
                'needs_improvement': '⚠️',
                'poor': '❌',
                'error': '🚫'
            }.get(review.get('overall_score', 'error'), '❓')
            
            comment_parts.extend([
                f"## {score_emoji} `{file_path}`",
                f"**Overall:** {review.get('summary', 'No summary available')}",
                ""
            ])
            
            # Issues
            issues = review.get('issues', [])
            if issues:
                comment_parts.append("### Issues Found:")
                for issue in issues[:5]:  # Limit to 5 issues per file
                    severity_emoji = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(issue.get('severity', 'medium'), '🟡')
                    line_info = f" (Line {issue.get('line')})" if issue.get('line') else ""
                    comment_parts.extend([
                        f"- {severity_emoji} **{issue.get('type', 'General').title()}**{line_info}: {issue.get('issue', '')}",
                        f"  💡 *Suggestion:* {issue.get('suggestion', '')}"
                    ])
                    if issue.get('example'):
                        comment_parts.append(f"  📝 *Example:* `{issue.get('example', '')}`")
                comment_parts.append("")
            
            # Positive aspects
            positive = review.get('positive_aspects', [])
            if positive:
                comment_parts.append("### ✨ Positive Aspects:")
                for aspect in positive[:3]:  # Limit to 3 positive aspects
                    comment_parts.append(f"- {aspect}")
                comment_parts.append("")
            
            # Key recommendations
            recommendations = review.get('recommendations', [])
            if recommendations:
                comment_parts.append("### 🎯 Key Recommendations:")
                for rec in recommendations[:3]:  # Limit to 3 recommendations
                    comment_parts.append(f"- {rec}")
                comment_parts.append("")
        
        # Footer
        comment_parts.extend([
            "---",
            "*This review was generated automatically by Claude Code following the [Google Developer Documentation Style Guide](https://developers.google.com/style).*",
            "",
            "📚 **Resources:**",
            "- [Google Developer Documentation Style Guide](https://developers.google.com/style)",
            "- [Markdown Best Practices](https://www.markdownguide.org/basic-syntax/)",
            "- [Technical Writing Guidelines](https://developers.google.com/tech-writing)"
        ])
        
        return "\n".join(comment_parts)
    
    def run_review(self, changed_files: List[str], head_sha: str) -> Dict[str, Dict[str, Any]]:
        """Run review on changed documentation files"""
        reviews = {}
        
        # Filter to documentation files
        doc_files = [f for f in changed_files if f.endswith(('.md', '.markdown', '.rst'))]
        
        if not doc_files:
            logger.info("No documentation files found to review")
            return reviews
        
        logger.info(f"Reviewing {len(doc_files)} documentation files")
        
        for file_path in doc_files:
            logger.info(f"Reviewing {file_path}")
            
            # Get file content
            content = self.get_file_content(file_path, head_sha)
            if not content:
                logger.warning(f"Could not get content for {file_path}")
                continue
            
            # Skip very short files (likely not documentation)
            if len(content.strip()) < 100:
                logger.info(f"Skipping {file_path} - too short")
                continue
            
            # Review the content
            review = self.review_file(file_path, content)
            reviews[file_path] = review
            
            logger.info(f"Completed review of {file_path}: {review.get('overall_score', 'unknown')}")
        
        return reviews

def main():
    parser = argparse.ArgumentParser(description='Claude Code Documentation Reviewer')
    parser.add_argument('--changed-files', required=True, help='Space-separated list of changed files')
    parser.add_argument('--pr-number', required=True, help='Pull request number') 
    parser.add_argument('--base-sha', required=True, help='Base commit SHA')
    parser.add_argument('--head-sha', required=True, help='Head commit SHA')
    
    args = parser.parse_args()
    
    try:
        # Initialize reviewer
        reviewer = ClaudeDocsReviewer()
        
        # Parse changed files
        changed_files = [f.strip() for f in args.changed_files.split() if f.strip()]
        
        logger.info(f"Starting review for PR #{args.pr_number}")
        logger.info(f"Changed files: {changed_files}")
        
        # Run review
        reviews = reviewer.run_review(changed_files, args.head_sha)
        
        # Generate comment
        comment = reviewer.format_review_comment(reviews)
        
        # Save results
        results_file = '/tmp/claude-review-results.md'
        with open(results_file, 'w') as f:
            f.write(comment)
        
        logger.info(f"Review completed. Results saved to {results_file}")
        logger.info(f"Reviewed {len(reviews)} files")
        
        # Log summary
        if reviews:
            scores = [r.get('overall_score') for r in reviews.values()]
            logger.info(f"Review scores: {dict(zip(reviews.keys(), scores))}")
        
    except Exception as e:
        logger.error(f"Review failed: {e}")
        
        # Create error comment
        error_comment = f"""🤖 **Claude Code Documentation Review**

❌ **Review Failed**

An error occurred while reviewing the documentation:
```
{str(e)}
```

Please check the workflow logs for more details."""
        
        with open('/tmp/claude-review-results.md', 'w') as f:
            f.write(error_comment)
        
        sys.exit(1)

if __name__ == '__main__':
    main()