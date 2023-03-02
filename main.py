#!/bin/python2

import os, sys, time, requests, random
import log as mysploitx

def main():
  try:
    import requests
    try:
      import yaml
      from yaml.loader import SafeLoader
      try:
        with open("assets/msg.yml", "r") as msg:
          msgData = yaml.load(msg, Loader=SafeLoader)
          try:
            #PROGRAM CHECK SERVER
            req = requests.get("{}/server2.txt".format(msgData["url"]), timeout=1)
            if req.status_code < 200 or req.status_code >= 250:
              mysploitx.log(msgData["msgServerNotFound"])
            else:
              try:
                #PROGRAM LOGIN
                checkUser = open("/data/data/com.termux/.user.yml", "r").read()
              except IOError:
                #PROGRAM REGISTER
                try:
                  req = requests.get("{}/server2.txt".format(msgData["url"]), timeout=1)
                  if req.status_code < 200 or req.status_code >= 250:
                    mysploitx.log(msgData["msgServerNotFound"])
                  else:
                    fileListUsers = open(".listUsers.txt", "w")
                    fileListUsers.write(req.text)
                    fileListUsers.close()
                    checkUsername = open(".listUsers.txt", "r").read()
                    usernameRegister = raw_input("[+] Username: ")
                    passwordRegister = raw_input("[+] Password: ")
                    casswordRegister = raw_input("[+] Comfirm Password: ")
                    if usernameRegister in checkUsername:
                      mysploitx.log(msgData["msgUsernameAlreadyInUse"])
                    else:
                      if passwordRegister == casswordRegister:
                        num = "0123456789"
                        createIP1 = "".join(random.sample(num, random.randint(2,3)))
                        createIP2 = "".join(random.sample(num, random.randint(2,3)))
                        createIP3 = "".join(random.sample(num, random.randint(2,3)))
                        createIP4 = "".join(random.sample(num, random.randint(2,3)))
                        getIP = "{}.{}.{}.{}".format(createIP1, createIP2, createIP3, createIP4)
                        dataUser = {
                          "Username": usernameRegister,
                          "Password": passwordRegister,
                          "Balance": 0,
                          "IP": getIP
                        }
                        with open("/data/data/com.termux/.user.yml", "w") as register:
                          data = yaml.dump(dataUser, register, sort_keys=True)
                          try:
                            dataListUsers = open(".listUsers.txt", "w")
                            dataListUsers.write("{}\n".format(usernameRegister))
                            dataListUsers.close()
                            dataListUsers = open(".listUsers.txt", "r").read()
                            s = requests.Session()
                            req = s.put("{}/server2.txt".format(msgData["url"]), data=dataListUsers, timeout=1)
                            if req.status_code < 200 or req.status_code >= 250:
                              mysploitx.log(msgData["msgErrorFailedCreateAccount"])
                              os.system("rip /data/data/com.termux/.user.yml")
                            else:
                              try:
                                dataUser = open("/data/data/com.termux/.user.yml", "r").read()
                                s = requests.Session()
                                req = s.put("{}/{}.txt".format(msgData["url"], getIP), data=dataUser, timeout=1)
                                if req.status_code < 200 or req.status_code >= 250:
                                  mysploitx.log(msgData["msgErrorFailedCreateAccount"])
                                  os.system("rip /data/data/com.termux/.user.yml")
                                else:
                                  mysploitx.log(msgData["msgSuccessfulyCreateAccount"])
                                  time.sleep(2)
                                  os.system("python2 main.py")
                              except requests.exceptions.ReadTimeout:
                                mysploitx.log(msgData["msgReadTimeout"])
                              except requests.exceptions.ConnectionError:
                                mysploitx.log(msgData["msgConnectionError"])
                          except requests.exceptions.ReadTimeout:
                            mysploitx.lof(msgData["msgReadTimeout"])
                          except requests.exceptions.ConnectionError:
                            mysploitx.log(msgData["msgConnectionError"])
                      else:
                        mysploitx.log(msgData["msgPasswordInValid"])
                except requests.exceptions.ReadTimeout:
                  mysploitx.log(msgData["msgReadTimeout"])
                except requests.exceptions.ConnectionError:
                  mysploitx.log(msgData["msgConnectionError"])
          except requests.exceptions.ReadTimeout:
            mysploitx.log(msgData["msgReadTimeout"])
          except requests.exceptions.ConnectionError:
            mysploitx.log(msgData["msgConnectionError"])
      except IOError as err:
        print(err)
        #mysploitx.log("[!] File msg.yml tidak di temukan.")
    except ImportError:
      mysploitx.log("[!] Install pyyaml dan coba lagi.")
  except ImportError:
    mysploitx.log("[!] Install requests dan coba lagi.")
main()