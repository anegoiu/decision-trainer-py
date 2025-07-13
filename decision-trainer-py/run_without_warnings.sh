#!/bin/bash

# Set environment variables to suppress Python warnings
export PYTHONWARNINGS="ignore::DeprecationWarning,ignore::PendingDeprecationWarning,ignore::FutureWarning,ignore::SyntaxWarning"
export UV_NO_PROGRESS=1

echo "🔇 Running crew with warnings suppressed..."
echo "📝 To see warnings, run: uv run run_crew"
echo

# Run the crew with uv
uv run run_crew "$@" 