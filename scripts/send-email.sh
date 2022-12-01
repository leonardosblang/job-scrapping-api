ls
echo "Installing mailutils ..."
sudo apt-get install mailutils
echo "New commit!" | mail -s "subject: Job Scrapping API" PERSONAL_EMAIL