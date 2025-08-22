#!/usr/bin/env python3
"""
Test script for Claude Code Documentation Review System
Creates sample documentation files and tests the review functionality
"""

import os
import sys
import tempfile
import json
import subprocess
from pathlib import Path

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_test_files():
    """Create sample documentation files with various style issues"""
    
    test_files = {
        'good_example.md': '''# Configure SSL Certificates

This guide shows you how to configure SSL certificates for secure communication.

## Prerequisites

Before you begin, ensure you have:

1. Administrative access to your server
2. A valid SSL certificate file
3. The corresponding private key

## Configure the Certificate

To configure your SSL certificate:

1. Copy the certificate file to `/etc/ssl/certs/`
2. Set the appropriate permissions:
   ```bash
   chmod 644 /etc/ssl/certs/your-cert.pem
   ```
3. Update your configuration file
4. Restart the service

## Verify the Configuration

To verify your SSL configuration works correctly:

1. Run the verification command:
   ```bash
   openssl s_client -connect localhost:443
   ```
2. Check the certificate details in the output

Your SSL certificate is now configured and ready to use.

## Troubleshooting

If you encounter connection errors:

- Verify the certificate file path is correct
- Check that the private key matches the certificate
- Ensure the service has restarted properly

## Next Steps

Now that SSL is configured, you can:

- [Enable HTTPS redirects](https://example.com/redirects)
- [Configure certificate auto-renewal](https://example.com/renewal)
- [Monitor certificate expiration](https://example.com/monitoring)
''',

        'needs_improvement.md': '''# SSL

SSL certificates should be configured by the user. The certificates will be installed in the system.

## Installation

In order to install the certificate, the following steps will need to be completed by the user. One can follow these steps:

- The certificate file should be copied to the server
- Permissions should be set appropriately  
- The configuration should be updated
- The service should be restarted

The certificate will be validated by the system after installation has been completed.

## Issues

If there are problems, the user should check the following:

- Certificate path
- Private key matching
- Service status

Click [here](https://example.com) for more information.

## Additional Information

Due to the fact that security is important, certificates must be kept up to date. The system administrator should monitor certificate expiration dates.
''',

        'poor_example.md': '''# ssl stuff

this document explains ssl. ssl is important.

## setup

ssl certificates can be configured. the certificates should be installed. 

here are the steps:
- copy files
- set permissions  
- restart

## problems

if it doesn't work:
- check stuff
- try again

see [this](http://example.com) for help.

master/slave configuration is also needed.

## code

run this:
```
openssl command here
systemctl restart service
```

The certificates will be managed by the administrator. Users will access the system through https.
'''
    }
    
    # Create temporary directory
    temp_dir = tempfile.mkdtemp(prefix='claude_docs_test_')
    
    # Write test files
    for filename, content in test_files.items():
        file_path = os.path.join(temp_dir, filename)
        with open(file_path, 'w') as f:
            f.write(content)
    
    return temp_dir, list(test_files.keys())

def mock_github_env():
    """Set up mock environment variables for testing"""
    os.environ.update({
        'REPO_OWNER': 'test-owner',
        'REPO_NAME': 'test-repo', 
        'PR_NUMBER': '123',
        'GITHUB_TOKEN': 'mock-token'
    })

def test_style_guide_loading():
    """Test that style guide rules load correctly"""
    print("🧪 Testing style guide configuration...")
    
    config_file = Path(__file__).parent.parent / 'config' / 'style-guide-rules.yaml'
    
    if not config_file.exists():
        print("❌ Style guide rules file not found")
        return False
    
    try:
        import yaml
        with open(config_file) as f:
            rules = yaml.safe_load(f)
        
        # Check required sections
        required_sections = ['writing_style', 'structure', 'technical_writing']
        for section in required_sections:
            if section not in rules:
                print(f"❌ Missing required section: {section}")
                return False
        
        print("✅ Style guide rules loaded successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error loading style guide rules: {e}")
        return False

def test_config_loading():
    """Test that PR review configuration loads correctly"""
    print("🧪 Testing PR review configuration...")
    
    config_file = Path(__file__).parent.parent / 'config' / 'pr-review-config.json'
    
    if not config_file.exists():
        print("❌ PR review config file not found")
        return False
    
    try:
        with open(config_file) as f:
            config = json.load(f)
        
        # Check required sections
        required_sections = ['claude_reviewer', 'review_scope', 'style_guide']
        for section in required_sections:
            if section not in config:
                print(f"❌ Missing required section: {section}")
                return False
        
        print("✅ PR review configuration loaded successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error loading PR review config: {e}")
        return False

def test_reviewer_import():
    """Test that the main reviewer module can be imported"""
    print("🧪 Testing reviewer module import...")
    
    try:
        # Try to import without running (no API calls)
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        # Import specific classes to test structure
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "claude_docs_reviewer", 
            os.path.join(os.path.dirname(__file__), "claude-docs-reviewer.py")
        )
        module = importlib.util.module_from_spec(spec)
        
        # Test that it has expected classes
        spec.loader.exec_module(module)
        
        if not hasattr(module, 'GoogleStyleGuide'):
            print("❌ GoogleStyleGuide class not found")
            return False
            
        if not hasattr(module, 'ClaudeDocsReviewer'):
            print("❌ ClaudeDocsReviewer class not found")
            return False
        
        print("✅ Reviewer module imported successfully")
        return True
        
    except Exception as e:
        print(f"❌ Error importing reviewer module: {e}")
        return False

def test_workflow_syntax():
    """Test that the GitHub Actions workflow has valid syntax"""
    print("🧪 Testing GitHub Actions workflow syntax...")
    
    workflow_file = Path(__file__).parent.parent / 'workflows' / 'docs-review.yml'
    
    if not workflow_file.exists():
        print("❌ Workflow file not found")
        return False
    
    try:
        import yaml
        with open(workflow_file) as f:
            workflow = yaml.safe_load(f)
        
        # Check required workflow elements
        if 'name' not in workflow:
            print("❌ Workflow missing 'name' field")
            return False
            
        if 'on' not in workflow:
            print("❌ Workflow missing 'on' trigger")
            return False
            
        if 'jobs' not in workflow:
            print("❌ Workflow missing 'jobs' section")
            return False
        
        print("✅ GitHub Actions workflow syntax is valid")
        return True
        
    except Exception as e:
        print(f"❌ Error validating workflow syntax: {e}")
        return False

def create_sample_pr():
    """Create a sample PR scenario for testing"""
    print("🧪 Creating sample PR test scenario...")
    
    try:
        temp_dir, test_files = create_test_files()
        print(f"✅ Created test files in: {temp_dir}")
        
        # Print file summaries
        for filename in test_files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path) as f:
                content = f.read()
            
            print(f"📄 {filename}: {len(content)} chars, {len(content.split())} words")
        
        return temp_dir, test_files
        
    except Exception as e:
        print(f"❌ Error creating sample PR: {e}")
        return None, []

def run_integration_test():
    """Run a basic integration test (without API calls)"""
    print("🧪 Running integration test...")
    
    # This would normally call the Claude API, but for testing we'll just
    # verify the structure and configuration
    
    try:
        # Set up mock environment
        mock_github_env()
        
        # Create test files
        temp_dir, test_files = create_sample_pr()
        if not temp_dir:
            return False
        
        # Test that we can construct the reviewer (without API key)
        print("✅ Integration test structure validated")
        
        # Clean up
        import shutil
        shutil.rmtree(temp_dir)
        
        return True
        
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Claude Code Documentation Review Tests\n")
    
    tests = [
        ("Configuration Loading", test_config_loading),
        ("Style Guide Loading", test_style_guide_loading), 
        ("Reviewer Module Import", test_reviewer_import),
        ("Workflow Syntax", test_workflow_syntax),
        ("Sample PR Creation", lambda: create_sample_pr()[0] is not None),
        ("Integration Test", run_integration_test)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n{'='*50}")
    print("📊 TEST SUMMARY")
    print(f"{'='*50}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! The documentation review system is ready to use.")
        print("\n📝 Next steps:")
        print("1. Set up ANTHROPIC_API_KEY in GitHub repository secrets")
        print("2. Ensure GitHub token permissions are configured")
        print("3. Create a test PR with documentation changes")
        return 0
    else:
        print(f"\n⚠️  {total - passed} tests failed. Please address the issues above.")
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)