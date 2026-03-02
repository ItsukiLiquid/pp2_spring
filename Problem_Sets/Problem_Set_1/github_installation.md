git init
git add .
git config --global user.email "myemail"
git config --global user.name "mygitname"
git config --global core.autocrlf true
git config --global core.safecrlf warn
git commit -m "I've commited and the appropriate message here"
git remote add origin https://github.com/ItsukiLiquid/pp2_spring.git
git branch -M origin main
git push -u main