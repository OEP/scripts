#
# pytenv -- create throwaway Python virtual environments
#
# Creates a virtual environment using mktemp(1) and activates it. Extra
# arguments are passed along to virtualenv.
#

function pytenv() {
  local t=`mktemp -d -t pytenv.XXXXXX`
  virtualenv "$@" "$t"
  . "$t/bin/activate"
}
