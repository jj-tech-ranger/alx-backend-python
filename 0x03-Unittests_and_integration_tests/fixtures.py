#!/usr/bin/env python3
"""Fixtures for integration tests."""

ORG_PAYLOAD = {
    "login": "google",
    "id": 1342004,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "events_url": "https://api.github.com/orgs/google/events",
    "hooks_url": "https://api.github.com/orgs/google/hooks",
    "issues_url": "https://api.github.com/orgs/google/issues",
    "members_url": "https://api.github.com/orgs/google/members{/member}",
    "public_members_url": "https://api.github.com/orgs/google/public_members{/member}",
    "avatar_url": "https://avatars.githubusercontent.com/u/1342004?v=4",
    "description": "Google",
}

REPOS_PAYLOAD = [
    {"id": 1, "name": "repo1", "license": {"key": "apache-2.0"}},
    {"id": 2, "name": "repo2", "license": {"key": "mit"}},
    {"id": 3, "name": "repo3", "license": None},
    {"id": 4, "name": "repo4", "license": {"key": "apache-2.0"}},
]
