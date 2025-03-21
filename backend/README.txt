run
    python main.py

登录
curl -X POST http://127.0.0.1:5000/login -H 'Content-Type: application/json' -d '{"student_id":251430000,"password":"3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d"}'

查看个人课标
curl -v http://127.0.0.1:5000/schedule -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjU2NDU5MiwianRpIjoiNjA4MzJhNDktYTA4Yy00MGM3LTgyYWEtYTZlMDVhZGI3ZWM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MjUxNDMwMDAwLCJuYmYiOjE3NDI1NjQ1OTIsImV4cCI6MTc0MjU2NTQ5Mn0.Qd-g9rtIDxRV08Yv-jaeU84_WhYNfst3lssgg5vyCk8"

查看所有课程
curl http://127.0.0.1:5000/courses -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjU2NDU5MiwianRpIjoiNjA4MzJhNDktYTA4Yy00MGM3LTgyYWEtYTZlMDVhZGI3ZWM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MjUxNDMwMDAwLCJuYmYiOjE3NDI1NjQ1OTIsImV4cCI6MTc0MjU2NTQ5Mn0.Qd-g9rtIDxRV08Yv-jaeU84_WhYNfst3lssgg5vyCk8"

选课
curl -X POST http://127.0.0.1:5000/enroll -H 'Content-Type: application/json' -d '{"course_id":9035}' -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjU2NDU5MiwianRpIjoiNjA4MzJhNDktYTA4Yy00MGM3LTgyYWEtYTZlMDVhZGI3ZWM0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MjUxNDMwMDAwLCJuYmYiOjE3NDI1NjQ1OTIsImV4cCI6MTc0MjU2NTQ5Mn0.Qd-g9rtIDxRV08Yv-jaeU84_WhYNfst3lssgg5vyCk8"

退课
curl -X POST http://127.0.0.1:5000/drop -H 'Content-Type: application/json' -d '{"course_id":9035}' -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MjU2NTY2MywianRpIjoiMWEyMWNiMzMtYzBlMy00ZGM0LWFmNjUtZDQ3MDVlNmU3NTVlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MjUxNDMwMDAwLCJuYmYiOjE3NDI1NjU2NjMsImV4cCI6MTc0MjU2NjU2M30.KWBdCP3Gn4kcgkoSKuRXmF2dcSXvHrHjSAUNHFOVCIk"


mysql
    user: root  password: root
    创建数据库 create database course_selection_db;
    导入数据 ./mysql -uroot -p course_selection_db< Distributed-System-Project/course_selection_system.sql


用户密码
    user password: 111111, SHA-1 encode: 3d4f2bf07dc1be38b20cd6e46949a1071f9d0e3d