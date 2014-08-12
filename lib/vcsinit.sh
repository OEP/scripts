#
# vcsinit - create various kinds of source control repositories
#
# By default, create Git, Mercurial, and Subversion repositories in a temporary
# directory, or a directory specified as the first argument.  A VCS type is
# skipped if the required executable is not on $PATH.
#

vcsinit() {
  local dir="$1"
  if [ -z "$1" ]; then
    dir=`mktemp -d -t vcsinit.XXXXXX`
  fi
  pushd "$dir" > /dev/null
  mkdir -p git hg svn

  if type git 2>&1 >/dev/null; then
    mkdir git
    git init --bare git/main > /dev/null
    git clone git/main git/work &> /dev/null
  fi

  if type hg 2>&1 >/dev/null; then
    mkdir hg
    hg init hg/main > /dev/null
    hg clone hg/main hg/work > /dev/null
  fi

  if type svnadmin 2>&1 >/dev/null; then
    mkdir svn
    svnadmin create svn/main > /dev/null
    svn co "file://$dir/svn/main" svn/work > /dev/null
  fi
  echo "$dir"
  popd > /dev/null
}
