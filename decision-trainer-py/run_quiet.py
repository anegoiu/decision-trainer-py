#!/usr/bin/env python3
"""
Run the CrewAI project with all warnings suppressed.
Usage: python run_quiet.py [args]
"""
import sys
import os
import warnings

# Suppress ALL warnings before importing anything else
warnings.simplefilter("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Run the crew with all warnings suppressed."""
    print("🔇 Running CrewAI with warnings suppressed...")
    
    try:
        # Import and run the crew
        from decision_trainer.main import run
        run()
    except Exception as e:
        print(f"❌ Error running crew: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 