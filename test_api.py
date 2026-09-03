#!/usr/bin/env python3
"""Test script to verify Google Gemini API key is loaded and working."""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# Test 1: Check if Google Gemini API key is loaded
print("=" * 70)
print("TEST 1: Checking if Google Gemini API key is loaded...")
print("=" * 70)

google_key = os.getenv('GOOGLE_API_KEY')

if google_key:
    masked_key = f"{google_key[:7]}...{google_key[-4:]}"
    print(f"✅ Google Gemini API Key found: {masked_key}")
else:
    print("❌ Google Gemini API Key NOT found!")
    print("   Make sure you have a .env file with GOOGLE_API_KEY=your-key-here")
    exit(1)

# Test 2: Try to initialize the ChatGoogleGenerativeAI model
print("\n" + "=" * 70)
print("TEST 2: Initializing Google Gemini model...")
print("=" * 70)

try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    print("✅ ChatGoogleGenerativeAI initialized successfully")
except Exception as e:
    print(f"❌ Failed to initialize ChatGoogleGenerativeAI: {e}")
    exit(1)

# Test 3: Make a simple API call
print("\n" + "=" * 70)
print("TEST 3: Making a test API call...")
print("=" * 70)

try:
    response = llm.invoke("Say 'Hello from Google Gemini!' in exactly those words.")
    result = response.content
    print(f"✅ API call successful!")
    print(f"   Response: {result}")
except Exception as e:
    print(f"❌ API call failed: {e}")
    exit(1)

# All tests passed
print("\n" + "=" * 70)
print("🎉 ALL TESTS PASSED!")
print("=" * 70)
print("Your Google Gemini API is properly configured and working!")
