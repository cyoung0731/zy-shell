fz_src_dir="/d/huanyi/fz_server"
fz_vm_dir="/e/dev/git/fangzhou_vm/fangzhou_server"

cd $fz_vm_dir
ls | xargs rm -rf

cd $fz_src_dir
fz_src=$(ls)
echo $fz_src
cp -r $fz_src $fz_vm_dir

cd $fz_vm_dir
git status
git add .
git commit -m "更新时间$(date "+%Y-%m-%d %H:%M:%S")"
git push
