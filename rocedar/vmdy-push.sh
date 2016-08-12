dy_src_dir="/d/rocedar/git/appserver"
dy_vm_dir="/e/dev/git/dongya-vm/dongya_server"

cd $dy_vm_dir
ls | xargs rm -rf

cd $dy_src_dir
dy_src=$(ls)
echo $dy_src
cp -r $dy_src $dy_vm_dir

cd $dy_vm_dir
git status
git add .
git commit -m "更新时间$(date "+%Y-%m-%d %H:%M:%S")"
git push
