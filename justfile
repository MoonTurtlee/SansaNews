set dotenv-load

python := ".venv/bin/python3"

# Run dev server
dev:
	bun run dev

# Check if user is available
check username:
	{{python}} backend.py check {{username}}

# Get user media
get username:
	{{python}} backend.py get {{username}}

# Get media from all users in USERS_PATH
get-all:
	{{python}} backend.py get --all
