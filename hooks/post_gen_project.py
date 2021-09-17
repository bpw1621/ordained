import subprocess

# TODO ...
# subprocess.run(['sphinx-apidoc', '-o', 'docs', 'src'])

version_tag = 'v{{cookiecutter.version}}'
git_remote = 'git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git'

subprocess.run(['git', 'init'])
subprocess.run(['git', 'add', '-A'])
subprocess.run(['git', 'commit', '-m' 'Initial project commit'])
subprocess.run(['git', 'tag', version_tag])
subprocess.run(['git', 'remote', 'add', 'origin', git_remote])

# TODO unless the repository is created on github ahead of time this will fail
# TODO looks like curl -u 'USER' https://api.github.com/user/repos -d '{"name":"REPO"}'
# TODO would do it but not sure I want to assume the user has curl at the ready ...
# git_push_command = ['git', 'push', '-u', 'origin', 'master', version_tag]
# if input(f'{" ".join(git_push_command)}? [no]:').lower().startswith('y'):
#     subprocess.run(git_push_command)

# TODO print statement about what to do next ...
