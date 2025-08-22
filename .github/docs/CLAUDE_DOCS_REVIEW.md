# Claude Code Documentation Review System

This repository includes an automated documentation review system powered by Claude Code that helps technical writers maintain high-quality documentation following the Google Developer Documentation Style Guide.

## 🎯 Overview

When technical writers open pull requests with documentation changes, the system automatically:

1. **Analyzes changed markdown files** for style guide compliance
2. **Provides actionable feedback** with specific suggestions
3. **Scores documentation quality** using consistent criteria
4. **Posts detailed review comments** directly on the PR
5. **Tracks improvements** over time

## 🚀 Features

### ✅ Automated Style Guide Checking
- **Active voice detection** - Identifies passive voice usage
- **Second person consistency** - Ensures direct reader address
- **Present tense verification** - Checks instruction tense
- **Clear heading analysis** - Reviews heading descriptiveness
- **Procedure structure** - Validates numbered vs. bulleted lists
- **Code formatting** - Ensures proper syntax highlighting
- **Link text review** - Checks for descriptive link text
- **Terminology consistency** - Identifies mixed terms
- **Inclusive language** - Promotes accessible language

### 📊 Quality Scoring
- **Comprehensive scoring** based on Google Style Guide adherence
- **Severity levels** (High/Medium/Low) for prioritizing fixes
- **File-level assessments** with overall PR summary
- **Improvement tracking** across iterations

### 💬 Intelligent PR Comments
- **Actionable suggestions** with specific examples
- **Line-specific feedback** when possible
- **Positive reinforcement** for well-written sections
- **Resource links** to style guide documentation

## 🛠️ Setup Instructions

### Prerequisites
1. **Anthropic API Key** - Required for Claude Code integration
2. **GitHub Token** - For repository access and PR commenting
3. **Repository permissions** - Write access for automated comments

### Environment Variables
Set these in your GitHub repository secrets:

```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
GITHUB_TOKEN=${{ secrets.GITHUB_TOKEN }}  # Auto-provided by GitHub
```

### Configuration Files

#### 1. Workflow Configuration
Location: `.github/workflows/docs-review.yml`
- Triggers on PR changes to documentation files
- Runs the Claude Code review script
- Posts results as PR comments

#### 2. Style Guide Rules
Location: `.github/config/style-guide-rules.yaml`
- Comprehensive Google Developer Style Guide rules
- Configurable weights and priorities
- Examples and patterns for each rule

#### 3. Review Configuration
Location: `.github/config/pr-review-config.json`
- Claude model settings and parameters
- File patterns and exclusions
- Comment formatting preferences

## 📝 How It Works

### 1. Pull Request Trigger
When a PR is opened/updated with changes to:
- `docs/**/*.md` files
- `*.md` files in root
- `_includes/**` template files
- `_layouts/**` layout files

### 2. File Analysis
For each changed documentation file:
- Content is retrieved from GitHub API
- Claude analyzes against style guide rules
- Issues are identified with specific suggestions
- Positive aspects are highlighted

### 3. Review Generation
Results are compiled into:
- **Overall quality score** (Good/Needs Improvement/Poor)
- **Specific issues** with severity levels and suggestions
- **Positive feedback** on well-written sections
- **Key recommendations** for improvement

### 4. PR Comment
A comprehensive comment is posted including:
- Summary statistics and scores
- File-by-file breakdown
- Specific issues with line numbers (when available)
- Actionable suggestions and examples
- Links to relevant style guide resources

## 🎨 Example Review Output

```markdown
🤖 **Claude Code Documentation Review**
*Automated review following Google Developer Documentation Style Guide*

## 📊 Review Summary
- **Files reviewed:** 3
- **Good:** 1 📗
- **Needs improvement:** 2 📙
- **Poor:** 0 📕

## ✅ `docs/installation-guide.md`
**Overall:** Well-structured documentation with clear procedures

### ✨ Positive Aspects:
- Excellent use of numbered procedures for installation steps
- Clear, descriptive headings that guide the reader
- Proper code formatting with syntax highlighting

## ⚠️ `docs/api-reference.md`
**Overall:** Good content but needs style improvements

### Issues Found:
- 🟡 **Style** (Line 45): Use active voice instead of passive voice
  💡 *Suggestion:* Change "The API should be configured" to "Configure the API"
  📝 *Example:* `Configure the API to handle authentication requests`

- 🟡 **Terminology** (Line 67): Inconsistent terminology usage
  💡 *Suggestion:* Use "repository" consistently instead of mixing "repo" and "repository"

### 🎯 Key Recommendations:
- Convert passive voice constructions to active voice
- Maintain consistent terminology throughout the document
- Add more descriptive alt text for diagrams
```

## 🔧 Customization Options

### Adjusting Review Sensitivity
Edit `.github/config/pr-review-config.json`:

```json
{
  "quality_thresholds": {
    "good": 0.85,           // 85%+ score = Good
    "needs_improvement": 0.70, // 70-84% = Needs Improvement  
    "poor": 0.69            // <70% = Poor
  }
}
```

### Focusing on Specific Rules
Edit `.github/config/style-guide-rules.yaml`:

```yaml
writing_style:
  active_voice:
    enabled: true
    weight: high  # high/medium/low
```

### Customizing Comment Output
Modify the formatting in `claude-docs-reviewer.py`:
- Adjust max issues displayed per file
- Change severity emoji mappings
- Customize positive feedback sections

## 📈 Integration with Technical Writing Workflow

### For Technical Writers
1. **Create PR** with documentation changes
2. **Review automated feedback** within minutes
3. **Address high-priority issues** first
4. **Iterate and improve** based on suggestions
5. **Learn style patterns** for future writing

### For Reviewers
1. **Focus on content accuracy** instead of style
2. **Use automated feedback** as starting point
3. **Provide human insight** on complex topics
4. **Ensure consistency** across documentation

### For Documentation Managers
1. **Track quality trends** across PRs
2. **Identify common issues** needing training
3. **Maintain consistency** at scale
4. **Reduce review time** for style issues

## 🔍 Troubleshooting

### Common Issues

#### "Review Failed" Message
- Check that `ANTHROPIC_API_KEY` is set correctly
- Verify file permissions and repository access
- Review workflow logs for specific errors

#### No Review Comment Posted
- Ensure GitHub token has appropriate permissions
- Check that changed files match the file patterns
- Verify the PR includes actual documentation changes

#### Inconsistent Review Quality
- Review Claude model temperature settings
- Check if files are too large (>100KB limit)
- Ensure style guide rules are properly configured

### Debug Mode
Enable detailed logging by setting environment variable:
```bash
CLAUDE_REVIEW_DEBUG=true
```

## 📚 Resources

### Style Guides
- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Google Technical Writing Courses](https://developers.google.com/tech-writing)
- [Markdown Best Practices](https://www.markdownguide.org/basic-syntax/)

### Claude Code Documentation
- [Claude Code Overview](https://docs.anthropic.com/claude/docs/claude-code)
- [API Reference](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Best Practices](https://docs.anthropic.com/claude/docs/best-practices-for-anthropic-claude)

### GitHub Actions
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Security Best Practices](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

## 🤝 Contributing

### Improving the Review System
1. **Test with sample documentation** to identify edge cases
2. **Add new style guide rules** to the configuration
3. **Enhance error handling** and user feedback
4. **Optimize performance** for large repositories

### Feedback and Issues
- Create GitHub issues for bugs or feature requests
- Share feedback on review accuracy and usefulness
- Suggest additional style guide rules to implement

---

*This documentation review system helps maintain high-quality technical documentation by leveraging Claude Code's advanced language understanding capabilities combined with established style guide best practices.*