This guide walks you through setting up a shared GCP project for *Elements of Data Visualization*. Only one person per group needs to complete the setup.

### Create a GCP project

1. Go to [https://console.cloud.google.com](https://console.cloud.google.com) and log in using your gmail account (not your utexas account). If you do not have a gmail account, please create one now before proceeding.

2. Once logged in, if you have never used Google Cloud before, you will see the following: Click on **Try for Free**. GCP gives you $300 initially as a free trial, which is for your personal use. If you have used GCP before, you won't see this free trial option and you can skip to step 4. 

![](https://github.com/cs327e-spring2019/snippets/blob/master/Screenhots/Google%20Try%20for%20Free.PNG)

3. You can sign up for the free trial if you'd like, but you'll need to provide a credit card number to do that. Note that you will only be charged if you exceed the $300 credit. We will be creating a billing alert to avoid this issue.

4. Create a GCP project by clicking on the drop-down at the top of the page and selecting new project. If you signed up for the free trial, a GCP project should have been created for you by the name of **My First Project**. 

5. Change the name of your project to match your group name. To rename the GCP project, click on the three dots on the top right on the navigation bar and click on **Project Settings** in the dropdown.

![](https://github.com/cs327e-spring2019/snippets/blob/master/Screenhots/three%20dots.PNG)

6. Under **Settings**, you will be able to rename the project. 

### Grant permissions on your project

7. Click on the navigation menu on the top-left corner, select **IAM & admin**, and navigate to the **IAM** menu.

8. Click on **Grant access** to add the instructors to your GCP Project. 

9. In the **New Members** input box, enter scohen@utexas.edu and gaotengzhao@gmail.com. Under **Role**, select the **Project Owner** role and save.

10. Repeat the previous steps to grant your project partner access to the project. Assign them the **Project Owner** role and save. 

### Requesting a GCP coupon

11. Retrieve your GCP coupon from the [Student Coupon Retrieval Link](https://vector.my.salesforce-sites.com/GCPEDU?cid=JU6PADGfpQ2SBpfzLaBiVEO9jSNvD8e8fhQ0iIcRxcyrCMpKouvz%2FVhT2Rp6R8NX/).  

12. After submitting the form, you should receive an email shortly, asking you to verify your email; upon verification, you will receive your coupon code by email.

### Activating your coupon

13. Before moving forward, please ensure that you are logged in with your gmail account and not your utexas.edu account.

**Very Important: The utexas.edu account should ONLY be used for retrieving your coupon code. The activation of the coupon must be done with your gmail account. If you have any questions about this, please stop here and ask for help.**

14. Once you receive your coupon code, log out of your utexas account and log in with your gmail account before activating your coupon. Go to [https://console.cloud.google.com/education](https://console.cloud.google.com/education) to activate your coupon.

15. Enter your coupon code into the form and click Accept and Continue. This will activate the coupon and an Education billing account will be created.

### Linking your GCP Project to your billing account

If you are new to Google Cloud and have signed up for the free trial, you can skip this section as your project should already be linked to your billing account. Please proceed to the next section. 

16. Click on the billing menu

17. Look for My Projects on the Billing dashboard

18. Locate your GCP Project and click on the three dots next to it.

19. Select 'Change billing' and choose your billing account from the dropdown and, click on Set Account.


### Create a billing alert

Create a billing alert so that you can be alerted when you are running low on credits (and before you run out). 

20. Click on the navigation menu on the top-left corner, select **Billing**. 

21. In the search box at the top of the page, type **Budgets & alerts** and click on the product page that comes up. 

22. Choose **Billing Account for Education** from the drop-down menu (or **My Billing Account** if you signed up for the free trial) and click on **Go to Budgets and alerts** page. 

23. Click on the Create Budget button and fill out the form as follows:
    * Budget name: DW budget
    * Time range: Custom range
    * From: Accept the default, which should be today's date
    * To: No end date
    * Projects: Select your project from the drop-down or if you can't select it, keep the default
    * Services: All services (1795)
    * Uncheck 'Savings programs'
    * Uncheck 'Other savings'
    * Click next
    * Budget type: Specified amount
    * Target amount: $50
    * Keep the default alert thresholds of 50%, 90%, and 100%. 
    * Choose 'email alerts to project owners' or 'email alerts to billing admins and users'
    * Click Finish



