# Nubank spendings dashboard
----------------------------------------------------------------

**whys and acknowledgments**
----------------------------------------------------------------

The main reason I did this was to help organize our home expenses in a more automated way

But ended up being a nice way of learning how to design a dashboard with flexdashboard, shiny and some touches of css

There still a lot to do, like adding more "smart" metrics and making it more intuitive to run(oportunity to learn docker and some homeserver stuff).

Thanks @andreroggeri for creating the Pynubank library with nice documentation and intuitive and easy to use functions 

----------------------------------------------------------------

**Running**
----------------------------------------------------------------

To run the dashboard with the mock data is simple, just type `rmarkdown::run("Dasboard.Rmd")` in Rstudio console and in some seconds it should open

--------------------------------------------------------------

If you want to try it with your own data, you have to follow these steps:


1 Run *NubanksSetup(first time only).py* You should inspect the code and comment out the packages that are already installed.

	- It will execute the CLI made by adreoroggeri asking you the credentials of your account

	- after login, it will create a certificate named *cert.p12*


2 Open *get_data.py* in a IDE and:

	-replace "seuCPF_apenas_numeros_" with your CPF as a string, and "suasenha" with your password as a string aswell. 

	-you can run the script now(it will create a csv of all your credit card transactions), but the dashboard code calls it everytime you start it 


3 Open *Dashboard.Rmd* and:

	-Remove the comment from the `#reticulate::py_run_file(glue("{here()}/get_data.py"))`

	-Write `rmarkdown::run("Dasboard.Rmd")` and you should be good

	