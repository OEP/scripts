#
# mkrepo - make an Apt repository
#
mkrepo() {
  local root="./"
  local dist=$(lsb_release -cs)
  local component=main
  if [ $# -ge 1 ]; then
    root="$1"
  fi
  if [ $# -ge 2 ]; then
    dist="$2"
  fi
  if [ $# -ge 3 ]; then
    component="$3"
  fi
  mkdir -p "${root}/conf"
  cat >"${root}/conf/distributions" <<EOF
Origin: ${dist} testing
Label: ${dist} testing
Codename: ${dist}
Architectures: i386 amd64
Components: ${component}
Description: Testing repository for ${dist}
EOF
}
