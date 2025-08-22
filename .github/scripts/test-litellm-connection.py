#!/usr/bin/env python3
"""
Quick test script to verify LiteLLM proxy connectivity
"""
import os
import sys
import requests

def test_litellm_connection():
    """Test connection to company LiteLLM proxy"""
    
    # Check for required environment variables
    litellm_base_url = os.getenv('LITELLM_BASE_URL', 'https://llm-dev.sonatype.com')
    litellm_api_key = os.getenv('LITELLM_API_KEY')
    
    if not litellm_api_key:
        print("❌ LITELLM_API_KEY environment variable not set")
        return False
    
    print(f"🔍 Testing connection to: {litellm_base_url}")
    print(f"🔑 Using API key: {litellm_api_key[:8]}...")
    
    url = f"{litellm_base_url.rstrip('/')}/v1/chat/completions"
    
    headers = {
        'Content-Type': 'application/json',
        'x-litellm-api-key': litellm_api_key
    }
    
    payload = {
        'model': 'claude-3-sonnet-20240229',
        'messages': [
            {
                'role': 'user',
                'content': 'Test connection - respond with "Connection successful"'
            }
        ],
        'max_tokens': 50
    }
    
    try:
        print("📡 Making request to LiteLLM proxy...")
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        
        print(f"📊 Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                print(f"✅ Success! Response: {content}")
                return True
            else:
                print(f"❌ Unexpected response format: {result}")
                return False
        else:
            print(f"❌ Request failed: {response.status_code}")
            print(f"📄 Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing LiteLLM Proxy Connection")
    print("=" * 40)
    
    success = test_litellm_connection()
    
    print("=" * 40)
    if success:
        print("✅ LiteLLM proxy connection test PASSED")
        sys.exit(0)
    else:
        print("❌ LiteLLM proxy connection test FAILED")
        sys.exit(1)