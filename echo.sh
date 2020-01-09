#!/usr/bin/env bash

echo 'deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib
            deb-src http://mirrors.aliyun.com/debian/ stretch main non-free contrib
            deb http://mirrors.aliyun.com/debian-security stretch/updates main
            deb-src http://mirrors.aliyun.com/debian-security stretch/updates main
            deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib
            deb-src http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib
            deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib
            deb-src http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib' > /etc/apt/sources.list
