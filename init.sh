#!/usr/bin/env bash


# init node server
echo "start manager GUI Server"
npm start &


# init manager-rpc server
echo "start manager RPC Server"
python manager.py &