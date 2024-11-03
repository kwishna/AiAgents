#! /bin/bash
read -p "Enter Student Name: " name
read -p "Enter Student RollNo: " rollno
read -p "Enter Student Age: " age
read -p "Enter Student Marks: " marks
read -n 3 -p "Enter Student Course Code (only 3 characters will be read): " course
read -s -p "Enter OTP: " otp
echo "Please confirm your details"
echo "------------------------------------------------"
echo "Student Name: $name"
echo "Student Rollno: $rollno"
echo "Student Age: $age"
echo "Student Marks: $marks"
echo "Student Course: $course"
echo "Student OTP: $otp"