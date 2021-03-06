# Command Manual
Here you will find a helpful guide to the current CLI (command line interface) 
commands with this application for each role with a description of the use case for that command.
### Notes:
   - Users will be referenced frequently in this doc, for more information on users go to
   the [users doc](./users.md)

## Login
To login to the command line you will have to be registered already by an administrator or supervisor. You will type:

`login <email> <password>` 

The first time logging in you will not have a password and will be prompted to enter a new one.

## Logout
If you are logged in and wish to logout you can simply type:

`logout`

And you will no longer be the active user.

## Create a course
- ***Role(s) needed:** Supervisor or Administrator*

As a supervisor or an administrator you can create a course for users to be assigned to using:

`create course "<course name>"`

Once a course is created you can assign TAs and instructors to it.

## Delete a course
- ***Role(s) needed:** Supervisor or Administrator*

As a supervisor or administrator you can delete a course using:

`delete course <course name>`

The course will no longer exist.


## Create a lab
- ***Role(s) needed:** Supervisor or Administrator*

As a supervisor or an administrator you can create a lab for users toe be assigned to using:

`create lab "<course name>" "<lab name>"`

Once a course is created you can assign TAs to it.

## Assign instructors/TAs to courses/labs
- ***Role(s) needed:** Supervisor or Instructor*

As a supervisor you will be able to assign instructors or TAs to courses using:

`assign course ta "<course name>" <email>`
`assign course instructor "<course name>" <email>`

And as a supervisor or instructor you will be able to assign TAs to labs using:

`assign lab "<course name>" "<lab name>" <email>`

As an instructor you will only be able to enter emails of your TAs, and the lab section 
has to exist before assignment.

## Create a user
- ***Role(s) needed:** Supervisor or Administrator*

As a supervisor or administrator you can create a user using: _(For another administrator or supervisor)_

`create user <email> <first name> <last name> <role> <phone number without special characters> "<address>"`

or: _(For a TA or instructor)_

`create user <email> <first name> <last name> <role> <phone number without special characters> "<address>" "<office hours>" "<office location>"`

Once the user is created then the user will be able to log in.

## Delete a user
- ***Role(s) needed:** Supervisor or Administrator*

As a supervisor or administrator you can delete a user using:

`delete user <email>`

The user will no longer be able to login again after they have been deleted

## Edit a user
- ***Role(s) needed:** Any* 

As a user you will be able to edit your account information using:

`edit <attribute>:"<new value>"`

But as a supervisor or administrator you will be able to edit any user's account using:

`edit user <email> <attribute>:"<new value>"`

## Notify a user
- ***Role(s) needed:** Supervisor, Administrator, or Instructor*

As a supervisor or administrator you will be able to send out an email to any user in the
system, but as an instructor you will only be able to email your TAs using:

`notify <email address> "<subject>" "<body>"`

## Viewing data
- ***Role(s) needed:** Any* 

As a user you will be able to view different information, but the commands you will be able to run
will depend on the role you have
 
#### Viewing individual things:
- *Viewing specific user data:* `view user <email>`
    - This will show different data based on the role.
    - As an Instructor or TA you will be able to see that user's public information
    - As a Supervisor or Administrator you will see all of that user's information
 
- *Viewing course assignments:* `view course "<course name>"`
    - As a Supervisor or Administrator you will be able to see any course with that course name
    - As an Instructor you will only see that course information if you're assigned to it
    - TAs will not be able to run this command
    
- *Viewing course assignments:* `view lab "<lab id>"`
    - As a Supervisor or Administrator you will be able to see any course with that course name
    - As an Instructor you will only see that lab information if you're assigned to it's course
    - TAs will not be able to run this command

#### Viewing lists of things:
- *Viewing specific user data:* `list users`
    - This will show different data based on the role.
    - As an Instructor or TA you will be able to see users' public information
    - As a Supervisor or Administrator you will see all information
 
- *Viewing specific user data:* `list tas`
    - This will do the same thing as the `view users` command, but will only show TAs
 
- *Viewing course assignments:* `list courses`
    - As a Supervisor or Administrator you will be able to see all course
    - As an Instructor you will only see courses that you're assigned to
    - TAs will not be able to run this command
    
- *Viewing course assignments:* `list labs`
    - As a Supervisor or Administrator you will be able to see all labs
    - As an Instructor you will only see the labs that are assigned to the course it's associated with
    - TAs will not be able to run this command
