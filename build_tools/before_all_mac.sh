# Check if running in GitHub Actions
if [ "$GITHUB_ACTIONS" = "true" ]; then
    brew update
fi

brew install eigen boost

bash build_tools/build_iqtree.sh