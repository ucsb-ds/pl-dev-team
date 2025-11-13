---
parent: Topics
layout: default
title: "Canvas"
description:  "Getting PrarieLearn grades into Canvas"
---

# {{page.title}} - {{page.description}}

Eventually, UCSB's implementation of PrairieLearn will feature direct integration with Canvas.

In the meantime though, if you want grades from PrarieLearn into your Canvas gradebook, you need to use an indirect method 
involving these eight steps, which we'll describe first at a high-level, then in detail.

1. Create the assignment in Canvas
2. Export the Grades as a .csv file
3. Import that CSV file into a Google Sheets spreadsheet
4. Export the Grades from PrarieLearn as a .csv file 
5. Import that CSV file into the same Google Sheets spreadsheet.
6. Configure the column in the Canvas sheet in the spreadsheet to pull the grades from the other sheet using `VLOOKUP`
7. Export that sheet as a CSV
8. Import that final CSV into Canvas.



## 1. Create the assignment in Canvas

Create an assignment in Canvas.  Leave the dates blank, and make the submission type: `No submission`

<img width="277" height="161" alt="image" src="https://github.com/user-attachments/assets/773e8aba-8f6e-460b-bbd7-a1b6e2cf8324" />
<img width="251" height="175" alt="image" src="https://github.com/user-attachments/assets/b6aba7ce-4a1c-40f1-abaa-e395790a30c2" />

You also need to "Publish" the assignment so that it shows up in the gradebook.

## 2. Export the Grades as a .csv file

Navigate to `Grades` and select `Export` then `Export Entire Gradebook`

<img width="911" height="220" alt="image" src="https://github.com/user-attachments/assets/bf3c1657-eef0-4536-aab7-6b3befe5f23e" />


## 3. Import that CSV file into a Google Sheets spreadsheet

Import this file into a Google Sheets spreadsheet.  The top left corner should look like this:

<img width="730" height="78" alt="image" src="https://github.com/user-attachments/assets/2abf119b-b89d-4411-84dc-1dde180bd7a0" />

## 4. Export the Grades from PrarieLearn as a .csv file 

Now, in PrairieLearn, navigate to your assessment.  Select the `Downloads` tab:

<img width="766" height="128" alt="image" src="https://github.com/user-attachments/assets/e8ffe8fc-96ae-4cf0-b635-f089f9522978" />

That should give you a page like this.  There are many more files than the ones shown in this screenshot, but the one you want is the one at the bottom of this screenshot, namely the one that ends in `_instances.csv`. Click that link and download that file:

<img width="756" height="265" alt="image" src="https://github.com/user-attachments/assets/683f4e6a-49ec-4994-a8e0-6e84c933b30e" />

## 5. Import that CSV file into the same Google Sheets spreadsheet.

Now, in your same Google Sheet where you imported the file from canvas, choose `File` : `Import`:

<img width="430" height="196" alt="image" src="https://github.com/user-attachments/assets/d0066348-415f-47d7-8119-4e8e4993dd45" />

Choose the file you downloaded from PrairieLearn (the one that ends in `_instance.csv`.

In the modal that pops up, select `Insert New Sheet`:

<img width="617" height="405" alt="image" src="https://github.com/user-attachments/assets/7bf8aead-9e11-48e1-8979-14425c77165a" />

So that it looks like this:

<img width="617" height="368" alt="image" src="https://github.com/user-attachments/assets/cd0b7044-8db5-4bd3-ad24-c0ac1ac01a46" />

You should now have the two files in the same spreadsheet, side by side like this:

<img width="844" height="48" alt="image" src="https://github.com/user-attachments/assets/cbdf7c52-bdc0-41e3-b7b7-76cd299450b9" />

To make things more clear, let's rename these tabs to `from-canvas` and `from-prairielearn`, like this:

<img width="392" height="58" alt="image" src="https://github.com/user-attachments/assets/0fd7d1fa-5831-4c93-b893-4c84993f14f4" />


## 6. Configure the column in the Canvas sheet in the spreadsheet to pull the grades from the other sheet using `VLOOKUP`

Now, find the column in the `from-canvas` spreadsheet for your Exam.  In the example, it's column `AN`, but it will likely be different in your sheet.

Note that the third row has `100` in it; this is important.  This should match the "possible points" (i.e. maximum grade) for your assessment.  If it doesn't, fix that in Canvas and here before proceeding.

<img width="137" height="219" alt="image" src="https://github.com/user-attachments/assets/94449701-a98f-4753-a5cd-d72f2c62f8fc" />

Now, in the cell under the `100`, the cell on the fourth line down, we'll put a formula to populate the grade.

For FERPA reasons, I'm not showing the values in my spreadsheet, but verify for yourself that:
* Row 4 has data for the first student
* Their UCSBNetId (i.e. their email without the `@ucsb.edu` part appears in column C and column D).

The formula we need is going to use that value to look up their grade and put it in the cell.

Verify that on your `from-prairielearn` tab, you have these column headings:

<img width="1158" height="60" alt="image" src="https://github.com/user-attachments/assets/f8f5f1cd-8fe1-4bb1b252-5f3fd0d9d6c5" />

You will see that:
* columm C (`Username`) on the `from-prairielearn` sheet matches column C on the `from-canvas` spreadsheet
* columns J and K on the `from-prairielearn` sheet have the score as a percentage and as a raw score.

So the formula for the basic score is this:

```
=VLOOKUP(C4,'from-prairielearn'!C:K,8,false)
```
Note:
* The `8` here signifies that column J is 8 columns over from column C where we started, so this pulls in the value of column J (percentage).  If we wanted column K (raw score), we'd use a `9`  in the formula instead.
* The `false` is important; it says that if we don't find an exact match, the value `N/A` will be reported.

The problem with this formula is that it will give us N/A values, which Canvas won't like.  So here's a slightly more complex formula that gets the job done.  

```
=IF(ISNA(VLOOKUP(C4,'from-prairielearn'!C:K,8,false)),0,VLOOKUP(C4,'from-prairielearn'!C:K,8,false))
```

It means this:

* If the value we looked up is NA, use 0, otherwise use the value.

Put this formulas into the 4th cell, and then drag it down to the bottom of the spreadsheet to the last student row.

You should now see that the values are populated correctly for the students.

## 7. Export that sheet as a CSV

Now, export this as a CSV, using the `File`/`Download`/`Comma Separated Values (.csv)` menu option in Google Sheets:

<img width="704" height="561" alt="image" src="https://github.com/user-attachments/assets/0f5c75f4-ebd3-460d-a898-c0f050bd3fc0" />


## 8. Import that final CSV into Canvas.

Now, return to Canvas to the Grades screen.   Use the Import button:

<img width="1139" height="156" alt="image" src="https://github.com/user-attachments/assets/602618ad-044f-4075-82bc-6bd3eccebbbc" />

This should import your grades into the Canvas grades spreadsheet.  Note that it can take 2-3 minutes for all of the grades to populate, so you may need to refresh the page a few times after the upload is complete.
