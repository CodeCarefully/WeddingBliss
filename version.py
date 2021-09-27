__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 2,
    'releaselevel': 'alpha',
    'serial': 1
}

import git


def get_version(short=False):
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0], __version_info__['serial']))
        repo = git.Repo(search_parent_directories=True)
        sha = repo.head.commit.hexsha
        short_sha = repo.git.rev_parse(sha, short=7)
        vers.append(" GIT:"+short_sha)
    return ''.join(vers)

__version__ = get_version()


if __name__ == '__main__':
    print(__version__ )
