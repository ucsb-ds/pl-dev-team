---
title: Software
description: "What you need to install"
layout: default
parent: info
---

# Software to Install or Configure (and/or update as needed)

Instructions on installing these follow below.

* The latest version of git
* Java 21
* Maven 3.9.9
* nvm (node version manager)
* Current LTS version of Node available through nvm (currently node v20.17.0, and npm v10.8.2)

## Recommmended for Everyone

1. Updated Zoom Client 

   Be sure that you have the *latest* version of the Zoom client.  Older versions may not have some of the features we'll need for this course.
    
   If you click on "About Zoom" inside zoom, you want a version that is 6.2.3 or later.
   
   Download it here: <https://zoom.us/download>

2. VSCode Text Editor for your local computer

   [Download link](https://code.visualstudio.com/download)

   While `vim` and `emacs` are perfectly fine for the work you may have done in CS16/24/32, when it comes to 
   professional level application development, it's time to graduate to some more professional tools.
   
   We have found that VSCode (a free download for Windows/Mac/Linux) is in the sweet spot between too few features, and too complicated.
  
   If you haven't worked with it before, we suggest you download it and start getting used to it.
   
   What it does for you:
   * Autocompletion
   * Syntax highlighting and checking
   * Automatic import detection
   * Ability to see an entire directory tree at once
   * Search and replace across multiple files
   * and much much more...
   
   Download it here: <https://code.visualstudio.com/download>

   Note: If you have **already** tried using VSCode and genuinely feel like you are more of a pro at `vim`, `nano`, `neovim`, or other project/code/text editors, feel free to use whatever is convenient for you. We are suggesting VSCode for ease of all-round use.
  
  
4. Install Java 21, Maven, and nvm on your local system.

   
   * For Mac users, instructions for installing with Homebrew appear below.   
   * For WSL users, see: [https://ucsb-cs156.github.io/topics/windows_wsl/](https://ucsb-cs156.github.io/topics/windows/windows_wsl.html)

   **You really do need Java 21, specifically**, and NOT Java 8, Java 11, Java 17, or a preview version of 22, 23, or higher.   It won't matter for the `"Hello World"` program in the first week, but when we move on to complex Java applications involving third-party libraries, it will definitely matter.
   
## Recommmended for Windows Users

Install Windows Subsystem for Linux.

It turns out that almost everything in terms of installing software (Java, Maven, Node, etc.) is easier under Linux than under native Windows.
Therefore we strongly suggest that if you have a Windows environment, you install the Windows Subsystem for Linux (WSL) and then follow the 
instructions under Linux/WSL.
   
If you are unable to install WSL because of limitations on your machine, please reach out to the course staff via Slack using the [#help-windows]({{site.help_windows_link}}) channel on Slack. In that case, we will try to find an alternative for you.
 
## Recommended for Ubuntu Linux / WSL Users
 
Instructions for installing Windows Subsystem for Linux (WSL), as well as environment setup instructions for Ubuntu systems, is available here: [https://ucsb-cs156.github.io/topics/windows_wsl/](https://ucsb-cs156.github.io/topics/windows/windows_wsl.html)

Native Ubuntu users (those not using Ubuntu through WSL) can skip the Windows-specific setup and go directly to [Install / Update Git on WSL](https://ucsb-cs156.github.io/topics/windows/windows_wsl.html#install--update-git-on-wsl) and follow all instructions from there on.

The following programs will be installed in the above guide:

* The latest version of git
* Java 21
* Maven 3.9.9
* nvm (latest stable version)
* Current LTS version of Node installed via `nvm install --lts; nvm use --lts` (currently node v20.17.0, and npm v10.8.2)

If you're using a Linux distribution that is not Ubuntu (or a similar Debian-based distribution with access to `apt`), the commands listed in the setup guide linked above may not work. The staff cannot provide support on finding equivalent commands for your desired distribution, but community resources such as Stack Overflow can help here.

## Recommmended for MacOS Users

If you have questions about this section, please ask on the [`#help-macos`]({{site.help_macos_link}}) channel on the Slack

1. Command Line Tools XCode for MacOS, including `git`

   On MacOS, `git` typically gets installed as part of the "Command Line XCode Tools" the first time you ask to use it.  To be sure that `git` is installed,
   try typing:
   
   ```
   git --version
   ```
   
   If it shows something like this you are good (version number may vary, and is not important as far as we know):
   
   ```
   git version 2.24.3 (Apple Git-128)
   ```

   Otherwise, you might get a message that you need to install the XCode Command Line Tools, i.e. something like this:

   ![image](https://github.com/user-attachments/assets/8e37dd9c-afb0-4a64-8611-86e4b03b6409)

   In that case, please just follow the instructions given in the message.  Don't worry if it says it will take 72 hours for the install; if you start it and let it run for a minute or two, that estimate should come down to something reasonable quickly, but it still make take 10-15 minutes.

   When you are done, you should be able to type `git --version` at a command prompt and see something like:

   ```
   git version 2.24.3 (Apple Git-128)
   ```

3. Brew (package manager)

   For MacOS, we'll be installing several packages for Java and JavaScript (node) development.  
   In many cases, installing those is easier if you *first* install the brew package manager.
   
   To install `brew`, visit <https://brew.sh/> and follow the instructions.

   If `brew` is already installed, use `brew update` to update brew before continuing.
   
4. Install Java 21 with `brew`: first part
   
   To install Java with homebrew, use:
   
   ```
   brew update
   brew install openjdk@21
   ```
   
   When the command finishes, **you are not finished**.  Keep that terminal window open and do the next part
   immediately.

3. Install Java 21 with `brew`: **important second part**
   
   After this command finishes executing, there will be some lines printed on the terminal *similar* to, but
   not necessarily *identical* to these:

   ```
   For the system Java wrappers to find this JDK, symlink it with
   sudo ln -sfn /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-21.jdk

   openjdk@21 is keg-only, which means it was not symlinked into /opt/homebrew,
   because this is an alternate version of another formula.

   If you need to have openjdk@21 first in your PATH, run:
   echo 'export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc

   For compilers to find openjdk@21 you may need to set:
   export CPPFLAGS="-I/opt/homebrew/opt/openjdk@21/include"
   ```

   You will need to find theses line in the text outputted by `brew install openjdk@21`
   and run it in the terminal. It should be near the end of the output. 
  
   Make sure you copy the commands from **your terminal output**, and **not** from this web page, since they
   may be customized to your Mac OS version, the architecture of your machine, etc.

   * Note that the command that starts with `sudo ln -sfn ...` only has to be done once.
   * The `echo 'export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc` command puts a line in your
     `.zshrc` startup file.  That will not take effect unless/until you start a new terminal window.
   * The line `export CPPFLAGS="-I/opt/homebrew/opt/openjdk@21/include"` is also one that would go in your
     `.zshrc` file.

   Once you've done these, open a **new terminal window** so that the `~/.zshrc` file is read from again before
   you test whether the Java 21 compiler was installed properly, with this command:
   
   ```
   java -version
   ```

   If it worked, you should see something like this:

   ```
   pconrad@Phillips-MacBook-Air ~ % java --version
   openjdk 21.0.4 2024-07-16
   OpenJDK Runtime Environment Homebrew (build 21.0.4)
   OpenJDK 64-Bit Server VM Homebrew (build 21.0.4, mixed mode, sharing)
   pconrad@Phillips-MacBook-Air ~ % 
   ```

5. Maven

   After installing Java 21, you can use `brew` to install Maven:

   ```
   brew update
   brew install maven
   ```

   Or if you already have Maven installed, do this to upgrade your version to the latest one:

   ```
   brew update
   brew upgrade maven
   ```

   Then to check that it is installed, do:

   ```
   mvn --version
   ```

   Be sure that you have Maven version 3.9 or higher, as Java 21 requires this version to work.

   When you type `mvn --version` if you are getting a version of Java other than Java 21, the fix is described
   in [this article](https://euedofia.medium.com/fix-default-java-version-on-maven-on-mac-os-x-156cf5930078) but that article is a little out of date, so here's the updated instructions:

   For example, you do NOT want to see this:
   ```
   pconrad@Phillips-MacBook-Air ~ % mvn --version
   Apache Maven 3.9.9 (8e8579a9e76f7d015ee5ec7bfcdc97d260186937)
   Maven home: /opt/homebrew/Cellar/maven/3.9.9/libexec
   Java version: 23, vendor: Homebrew, runtime: /opt/homebrew/Cellar/openjdk/23/libexec/openjdk.jdk/Contents/Home
   Default locale: en_US, platform encoding: UTF-8
   OS name: "mac os x", version: "14.4.1", arch: "aarch64", family: "mac"
   pconrad@Phillips-MacBook-Air ~ % 
   ```

   That shows the correct Maven version (3.9.9) but the wrong Java version (23).
   
   To update the maven configuration, file, edit this file; note that the version number may be different
   by the time you are reading these instructions:

   ```
   vim /opt/homebrew/Cellar/maven/3.9.9/bin/mvn
   ```

   In that file, change the line that starts with `JAVA_HOME=` to this:

   ```
   JAVA_HOME="${JAVA_HOME:-$(/usr/libexec/java_home 21)}" exec "/opt/homebrew/Cellar/maven/3.9.9/libexec/bin/mvn" "$@"
   ```
   Or if you find that the above does not work after typing `mvn --version` then try:
    ```
   JAVA_HOME="${JAVA_HOME:-/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home}" exec "/usr/local/Cellar/maven/3.9.9/libexec/bin/mvn" "$@"
   ```
   For Apple Silicon (M1/M2/M3), try replacing the first `openjdk` with `openjdk@21`, like this:
    ```
   JAVA_HOME="${JAVA_HOME:-/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home}" exec "/opt/homebrew/Cellar/maven/3.9.9/libexec/bin/mvn" "$@"
   ```
    
   Again, you may need to adjust the version number `3.9.9` to whatever your version of Maven is.  After doing
   this, if you type `mvn --version` it should show Java 21, like this:

   ```
   pconrad@Phillips-MacBook-Air ~ % mvn --version
   Apache Maven 3.9.9 (8e8579a9e76f7d015ee5ec7bfcdc97d260186937)
   Maven home: /opt/homebrew/Cellar/maven/3.9.9/libexec
   Java version: 21.0.4, vendor: Homebrew, runtime: /opt/homebrew/Cellar/openjdk@21/21.0.4/libexec/openjdk.jdk/Contents/Home
   Default locale: en_US, platform encoding: UTF-8
   OS name: "mac os x", version: "14.4.1", arch: "aarch64", family: "mac"
   pconrad@Phillips-MacBook-Air ~ % 
   ```
   
4. nvm, Node, and npm

   Even if you already have node and npm installed on your computer, you should install Node Version Manager (nvm). The instructions for installing this are the same as those for Linux and WSL users, so please follow the instructions listed there.

   [Install nvm and Node on WSL](https://ucsb-cs156.github.io/topics/windows/windows_wsl.html#install-nvm-and-node-on-wsl)

   [Update npm on WSL](https://ucsb-cs156.github.io/topics/windows/windows_wsl.html#update-npm-on-wsl)


## Optional (for everyone)

1. UCSB VPN Client (Pulse Secure) 

   What it does:
   * Reroutes all your network traffic through the UCSB network, so that it appears that
     your machine is directly connected to the UCSB Campus network

   What it allows you to do:

   * Access the textbooks for the course online without having to buy them.
   * Mount your CSIL home directory as a shared network drive using Samba
   * Graphically remote into CSIL


   **Note:** In order to use Pulse Secure, you need to setup DUO (a two factor authentication app).
   Here is a link for the instructions on how to set it up: <https://www.it.ucsb.edu/getting-started-mfa-duo/enroll-push-notification>

   Where to get Pulse Secure:  <https://www.it.ucsb.edu/pulse-secure-campus-vpn/get-connected-vpn>

2. Samba Access to your CSIL home directory 

   What it does:

   * Mounts your CSIL home directory "as if" it were connected directly to your
     computer.


   What it allows you to do:
   * Click on files on CSIL and open them in software on your own machine
     (e.g. an editor such as Sublime Text, VSCode, or a web browser.)

   Where to get it:
   * You don't have to download anything (though you do need the UCSB VPN Client first)
   * Instead, follow the instructions here:

     | Platform | Text Instructions | YouTube Video Instructions |
     |-|-|-|
     | MacOS | [Text](https://ucsb-cs156.github.io/topics/csil_mount_drive_to_macOs_using_samba/)  | [Video](https://youtu.be/FTlxjhjwbt0) |
     | Windows | [Text](https://ucsb-cs156.github.io/topics/CSIL/csil_mount_drive_to_windows_using_samba.html) | [Video](https://www.youtube.com/watch?v=fgORcrGWBH0) |
     | Linux | (ask staff) | |
     {:.table .table-sm .table-striped .table-bordered}


