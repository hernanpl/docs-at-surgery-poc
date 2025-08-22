# Claude Code Integration for Automated Documentation Review

This repository now includes a comprehensive automated documentation review system powered by Claude Code that integrates seamlessly with your GitHub workflow for technical writers.

## 🎯 What's Included

### 🤖 Automated PR Reviews
- **Triggers automatically** when technical writers open PRs with documentation changes
- **Analyzes markdown files** against Google Developer Documentation Style Guide
- **Posts detailed feedback** directly on GitHub pull requests
- **Provides actionable suggestions** with specific examples

### 📋 Google Developer Style Guide Compliance
- ✅ **Active voice detection** - Identifies passive voice usage
- ✅ **Second person consistency** - Ensures direct reader address  
- ✅ **Present tense verification** - Checks instruction tense
- ✅ **Clear heading analysis** - Reviews heading descriptiveness
- ✅ **Procedure structure validation** - Numbered vs. bulleted lists
- ✅ **Code formatting checks** - Syntax highlighting verification
- ✅ **Link text review** - Descriptive link text validation
- ✅ **Terminology consistency** - Mixed term identification
- ✅ **Inclusive language promotion** - Accessibility improvements

## 📁 Implementation Files

### Core System
```
.github/
├── workflows/
│   └── docs-review.yml              # GitHub Actions workflow
├── scripts/
│   ├── claude-docs-reviewer.py      # Main review engine
│   └── test-docs-review.py          # Testing and validation
├── config/
│   ├── style-guide-rules.yaml       # Comprehensive style rules
│   └── pr-review-config.json       # Review configuration
├── docs/
│   └── CLAUDE_DOCS_REVIEW.md       # Complete documentation
└── requirements.txt                 # Python dependencies
```

### Workflow Integration
- **Triggers**: PR changes to `docs/**/*.md`, `*.md`, `_includes/**`, `_layouts/**`
- **Permissions**: Read content, write PR comments
- **Dependencies**: Anthropic API, GitHub API
- **Output**: Detailed markdown comments with actionable feedback

## 🚀 Quick Setup

### 1. Repository Secrets
Add to your GitHub repository secrets:
```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
# GITHUB_TOKEN is automatically provided
```

### 2. Enable Workflow
The workflow at `.github/workflows/docs-review.yml` will automatically:
- Detect documentation changes in PRs
- Run Claude Code analysis
- Post comprehensive review comments

### 3. Test the System
```bash
# Run validation tests
python3 .github/scripts/test-docs-review.py

# Create a test PR with documentation changes
```

## 💡 Example Review Output

When a technical writer opens a PR, they'll receive feedback like:

```markdown
🤖 **Claude Code Documentation Review**

## 📊 Review Summary
- **Files reviewed:** 2
- **Good:** 1 📗  
- **Needs improvement:** 1 📙

## ⚠️ `docs/installation-guide.md`
**Overall:** Good content but needs style improvements

### Issues Found:
- 🟡 **Style** (Line 23): Use active voice instead of passive voice
  💡 *Suggestion:* "Configure the API" instead of "The API should be configured"
  📝 *Example:* `Configure the API to handle authentication requests`

### 🎯 Key Recommendations:
- Convert passive voice to active voice for clarity
- Use numbered lists for sequential procedures
- Add descriptive alt text for images
```

## 🎨 Benefits for Technical Writers

### ✅ Immediate Feedback
- Get style feedback within minutes of opening a PR
- No waiting for human reviewers for basic style issues
- Focus review time on content accuracy and completeness

### 📈 Consistency at Scale
- Maintain uniform style across all documentation
- Learn Google Style Guide patterns through examples
- Reduce back-and-forth on style corrections

### 🎯 Prioritized Improvements
- High/Medium/Low severity levels guide focus
- Specific line numbers and suggestions
- Positive reinforcement for well-written sections

### 📚 Continuous Learning
- Links to style guide resources
- Examples of improved text
- Pattern recognition for future writing

## 🔧 Customization Options

### Adjust Review Sensitivity
Edit `.github/config/pr-review-config.json`:
```json
{
  "quality_thresholds": {
    "good": 0.85,
    "needs_improvement": 0.70, 
    "poor": 0.69
  }
}
```

### Focus on Specific Rules
Edit `.github/config/style-guide-rules.yaml`:
```yaml
writing_style:
  active_voice:
    enabled: true
    weight: high  # Prioritize this rule
```

### Customize Output Format
Modify `claude-docs-reviewer.py` to:
- Change comment formatting
- Adjust number of issues shown
- Customize positive feedback sections

## 🔍 Quality Metrics

The system provides:
- **File-level scores** (Good/Needs Improvement/Poor)
- **Issue severity classification** (High/Medium/Low)
- **Improvement tracking** across PR iterations
- **Style guide rule coverage** reporting

## 🤝 Integration with Existing Workflow

### For Technical Writers
1. Write documentation following normal process
2. Open PR with changes
3. Review automated feedback within minutes
4. Address high-priority issues first
5. Iterate based on suggestions

### For Documentation Reviewers
1. Use automated feedback as starting point
2. Focus on content accuracy vs. style
3. Provide human insight on complex topics
4. Ensure technical correctness

### For Documentation Managers
1. Track quality trends across team
2. Identify common training needs
3. Maintain consistency standards
4. Reduce manual review overhead

## 📊 Success Metrics

Track improvements through:
- **Reduced review cycles** for style issues
- **Improved consistency scores** across documentation
- **Faster PR merge times** for technical writers
- **Higher documentation quality ratings**

## 🔮 Future Enhancements

Potential improvements:
- **Integration with style guide updates**
- **Custom rule creation for organization-specific needs**
- **Learning from accepted/rejected suggestions**
- **Integration with documentation analytics**

## 📞 Support

### Resources
- [Complete Documentation](.github/docs/CLAUDE_DOCS_REVIEW.md)
- [Google Developer Style Guide](https://developers.google.com/style)
- [Claude Code Documentation](https://docs.anthropic.com/claude/docs/claude-code)

### Troubleshooting
- Run test script: `python3 .github/scripts/test-docs-review.py`
- Check GitHub Actions logs for workflow issues
- Verify API keys and permissions are set correctly

---

*This automated documentation review system helps technical writers maintain high-quality documentation by leveraging Claude Code's advanced language understanding capabilities with established style guide best practices.*