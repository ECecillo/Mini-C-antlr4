<!-- LTeX: language=en -->
# Using a virtual machine to develop/test in MIF08

We prepared a few VM in case you have trouble with your personal machines. They have all the tools installed (ANTLR, RISCV, Python & required modules). If you can work on your local machine, do so and do not use the VMs.

## Chose a VM

We prepared a few VMs for you. To balance the load between VMs, please use the VM corresponding to your group:

* Group A : 192.168.153.167
* Group B : 192.168.153.17
* Group C : 192.168.152.109
* If the VM from your group is broken, use 192.168.153.180

In the explanations below, please replace IP_VM with the IP of your VM.

## Connecting to the machines (to do before all alternatives below)

The VM are only accessible from within the university's network. From home, you need a workaround to connect: either use the VPN, or an SSH jump.

### Simplest option: use the VPN

1. [Activate the VPN](https://documentation.univ-lyon1.fr/vpn/linux/)
2. Launch the SSH command as if you were within the university:
```
ssh your-univ-username@IP_VM
```

### Alternative if the VPN doesn't work: SSH jump

1. Add the following lines to your `~/.ssh/config` :
```
Host IP_VM
ProxyCommand ssh -N -W %h:22 your-univ-username@linuxetu.univ-lyon1.fr
```
2. Launch the SSH command as if you were within the university (you'll need to enter your password twice):
```
ssh your-univ-username@IP_VM
```

## Copying from/to the machines

You don't have direct access to your account from the VM. Be carefull, files you leave on the VM are not backed up, and may be deleted if the VM crashes. **Always keep backups elswhere**.

From your local machine, you may copy stuff from a local directory to the remote one (**Warning:** this overwrites the content of the directory on the remote machine.):

```
rsync -av local-dir/ your-univ-username@IP_VM:vm/
```

Don't forget the `:` after the machine name, and the trailing `/` after both the source and destination directories.

Conversely, you may copy stuff from the VM to your local machine:

```
rsync -av your-univ-username@IP_VM:vm/ local-dir/
```

Obviously, you can also push your Git repository to a project on the forge (you won't be able to push to the teachers' repo, but you can create your own) and push/pull on the local and remote machines.

## Use VSCode locally to work on the VM

Unfortunately, this uses a substantial amount of disk space on the VM, use with caution.

1. Install the [remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension
2. Type <kbd>Control</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>, ">Remote-SSH: connect to host", and enter "your-univ-username@IP_VM", then <kbd>Enter</kbd> and enter your password.
3. Work as if you were working directly on the VM: edit files, open terminal to run commands, ...

## Work directly on the VM

1. Connect to the VM using `ssh your-univ-username@IP_VM`
2. Edit files using the `nano` code editor (*very* primitive, but simple to use and works in text mode), or `emacs`, or `vim`
3. Switch back to the shell using <kbd>Control</kbd> + <kbd>z</kbd>, switch back to the editor using `fg`.
