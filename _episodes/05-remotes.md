---
layout: episode
title: "Remotes and GitHub"
teaching: 20
exercises: 25
questions:
  - How does version control scale from 1 to N users per repository?
  - How can I easily set up a public repository online
  - How can I easily set up a local repository for my computer?
objectives:
  - "Student understands the concept of remotes"
  - "Student can add an initialized repository to GitHub"
  - "Student can create a bare repository on a local machine"
keypoints:
  - Todo
  - todo
---

## Food for thought
- Who maintains the server that synchronizes all the changes?
- What happens if two or more people change the same things at the same time?
- How could a limited number of people work on a feature without bothering
  others about it just yet?
---

## Remotes

As we have observed the git repository is in fact a directory on your
computer.

### Set up GitHub account

By now you should already have set up a GitHub account but if you haven't,
please do so [here](https://github.com/join).

### Set up SSH keys

SSH keys are a way to authenticate yourself to remote systems based on [public
key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography).

To summarize in public key cryptography you have two keys: a private key and a
public key. Anything encrypted with your public key can only be decrypted with
your private key. This feature can be used to create a secret message that only the
holder of the private key can decrypt and it is often used to authenticate
people when signing on to remote systems.

Another side effect is that anything encrypted with the private key can be
opened with the public key. This feature is used for digital signing of e.g.
annotated tags in git.

In most Unix-systems you can create a pair of digital keys using
```
$ ssh-keygen
```
This will create a pair of files under the **~/.ssh/** folder.
```
$ cd ~/.ssh
$ ls
config   id_rsa      id_rsa.pub  known_hosts
```

The file id_rsa is the private key and it should **never** be shared with
anyone.

The file id_rsa.pub is the public key and it is safe to publish to everyone.


