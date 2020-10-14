app_view = document.getElementById('app-view')
startTime()
login_stat = undefined
// Dom7
var $$ = Dom7;
// Init App
var app = new Framework7({
  id: 'ml.abhishekdas',
  root: '#app',
  theme: 'md',
  routes, routes,
});
eel.sendloginPage()
eel.expose(loginPage)
function loginPage(receivedUser) {
  firstName = receivedUser
  loginScreen = app.loginScreen.create({
    content: '<div class="login-screen"><div class="view"><div class="page login-screen-css"><div class="loginstatus"></div><div class="page-content login-screen-content"><div class="login-screen-title"><h2>Welcome back ' + `${firstName}` + '</h2></div><form id="password-form"><div class="list"><ul><li class="item-content item-input item-input-outline"><div class="item-inner"><div class="item-title item-floating-label">Password</div><div class="item-input-wrap"> <input id="passwordField" type="password" name="userPassword" required validate data-error-message="Enter a vaild password" data-validate-on-blur="true" placeholder="Your password"></div><input type="reset" style="display: none;" id="resetuserpassword"></div></li></ul></div></form><div class="list"><ul><li><button onclick="submitpasswordB()" class="button list-button">Sign In</button></li></ul><div class="block-footer"><h2>Pygranthalaya | Library Managament Software</h2></div></div></div></div></div></div>',
    on: {
      closed: function () {
        app_view.classList.remove('user-login')
      }
    }
  })
  loginScreen.open()
}
var passwordError = app.toast.create({
  text: 'Wrong password. Try again!',
  horizontalPosition: 'center',
  closeTimeout: 2000,
});
eel.expose(triggerpasswordError)
function triggerpasswordError() {
  passwordError.open()
  document.getElementById("resetuserpassword").click()
}
function submitpasswordB() {
  var userPassword = app.form.convertToData('#password-form');
  if (userPassword.userPassword.length !== 0) {
    if (login_stat == undefined) {
      eel.submituserPassword(userPassword.userPassword, 1);
    } else { eel.submituserPassword(userPassword.userPassword, 13); }
  } else {
    triggerpasswordError()
  }
}
eel.expose(triggerpasswordSuccess)
function triggerpasswordSuccess(uN, iN, iC, iP, iE, tT, tC, lM) {
  document.getElementById("resetuserpassword").click()
  userName = uN
  document.getElementById("instN").innerText = `${iN}`
  document.getElementById("instA").innerText = `${iC}` + " - " + `${iP}`
  document.getElementById("instE").innerText = `${iE}`
  document.getElementById("libT").innerText = "Total Titles : " + `${tT}`
  document.getElementById("libC").innerText = "Total Copies : " + `${tC}`
  document.getElementById("libM").innerText = "Library Members : " + `${lM}`
  document.getElementById("userN").innerText = "Administrator : " + `${userName}`
  login_stat = 2;
  profileB = app.actions.create({
    buttons: [
      // First group
      [
        {
          text: userName + ' - signed in',
          bold: true
        },
        {
          text: 'Sign out',
          onClick: function () { loginScreen.open() },
          bold: true
        }
      ],
      // Second group
      [
        {
          text: 'Cancel',
          color: 'red'
        }
      ]
    ]
  });
  $$('.profileB').on('click', function () {
    profileB.open();
  });

  loginScreen.close()
}
$$('.toggleStat').on('click', function (e) {
  $$('.libStats').toggleClass('display-none');
});
eel.expose(operationSuccessMsg)
function operationSuccessMsg(msg) {
  if (msg == 1) {
    $$('.opt-db').toggleClass('color-green');
    app.toast.create({
      text: 'Optimization Successfull!',
      horizontalPosition: 'center',
      closeTimeout: 4000,
    }).open();
  }
  if (msg == 2) {
    $$('.bkp-db').toggleClass('color-green');
    app.toast.create({
      text: 'Backup Successfull!',
      horizontalPosition: 'center',
      closeTimeout: 4000,
    }).open();
  }
}
var addTitleDataError = app.toast.create({
  text: 'Fill ACC number and Title they cannot be empty and ACC number has to be unique!',
  horizontalPosition: 'center',
  closeTimeout: 4000,
});
var addTitleDataSuccess = app.toast.create({
  text: 'Title successfully saved to database!',
  horizontalPosition: 'center',
  closeTimeout: 2000,
});
eel.expose(triggeraddTitleDataError)
function triggeraddTitleDataError() {
  addTitleDataError.open()
  document.getElementById("resetadtform").click()
  var today = new Date();
  addTitleDate.setValue([today]);
  app.progressbar.hide()
}
eel.expose(triggeraddTitleDataSuccess)
function triggeraddTitleDataSuccess(tT, tC, lM) {
  document.getElementById("libT").innerText = "Total Titles : " + `${tT}`
  document.getElementById("libC").innerText = "Total Copies : " + `${tC}`
  document.getElementById("libM").innerText = "Library Members : " + `${lM}`
  var today = new Date();
  addTitleDate.setValue([today]);
  addTitleDataSuccess.open()
  app.progressbar.hide()
}
var addMembersDataSuccess = app.toast.create({
  text: 'Member successfully saved to database!',
  horizontalPosition: 'center',
  closeTimeout: 2000,
});
var addMembersDataError = app.toast.create({
  text: 'Fill all the fileds with accurate data and the member may already exist with the same UID!',
  horizontalPosition: 'center',
  closeTimeout: 2000,
});
eel.expose(triggeraddMembersDataError)
function triggeraddMembersDataError() {
  addMembersDataError.open()
  document.getElementById("resetadmform").click()
  app.progressbar.hide()
}
eel.expose(triggeraddMembersDataSuccess)
function triggeraddMembersDataSuccess(ADMID, tT, tC, lM) {
  document.getElementById("libT").innerText = "Total Titles : " + `${tT}`
  document.getElementById("libC").innerText = "Total Copies : " + `${tC}`
  document.getElementById("libM").innerText = "Library Members : " + `${lM}`
  addMembersDataSuccess.open()
  app.dialog.create({
    title: 'The UID of the added member is : ' + ADMID,
    buttons: [
      {
        text: 'OK',
      },
    ],
  }).open();
  app.progressbar.hide()
}
var addTitleDate = app.calendar.create({
  inputEl: '#add-title-date',
  dateFormat: 'dd/mm/yyyy',
});
function submitadm() {
  addMembersData = app.form.convertToData('#add-members-form');
  if (addMembersData.LADMID.length !== 0 && addMembersData.LNAME.length !== 0) {
    eel.submitaddMembersData(addMembersData.LADMID, addMembersData.LNAME, addMembersData.LCLASS, addMembersData.LSECTION, addMembersData.LEMID)
    document.getElementById("resetadmform").click()
  } else {
    triggeraddMembersDataError()
  }
}
function titleDetails(ACCNO, ACCDATE, ISBN) {
  app.dialog.create({
    title: 'Details',
    text: 'The book was accessioned on : ' + ACCDATE + " and has ISBN number : " + ISBN,
    buttons: [
      {
        text: 'DELETE TITLE',
        onClick: function () { app.progressbar.show(); eel.deleteTitle(ACCNO) },
      },
      {
        text: 'OK',
      },
    ],
  }).open();
}
eel.expose(queryTitlesTable)
function queryTitlesTable(mode) {
  if (mode == 1) {
    titlesTable = $('#query-titles').DataTable();
  } else {
    titlesTable.destroy(); titlesTable.destroy();
  }

}
eel.expose(fillTitlesHead)
function fillTitlesHead() {
  titlesTableHead = document.getElementById('query-titles-table')
  titlesTableHead.innerHTML += '<table id="query-titles"><thead class="elevation-1"><tr id="query-titles-head"><th class="label-cell">ACCNO</th><th class="label-cell">ISSUED</th><th class="label-cell medium-only">TITLE</th><th class="label-cell medium-only">AUTHOR</th><th class="label-cell">TYPE</th><th class="label-cell">COPIES</th><th class="label-cell">DETAILS</th></tr></thead><tbody id="query-titles-body"></tbody></table>'
}
eel.expose(fillTitlesBody)
function fillTitlesBody(ACCNO, ISSUED, TITLE, AUTHOR, TYPE, COPIES, ACCDATE, ISBN) {
  titlesTableBody = document.getElementById('query-titles-body')
  LACCDATE = `'${ACCDATE}'`; LISBN = `'${ISBN}'`;
  titlesTableBody.innerHTML += '<td class="label-cell">' + `${ACCNO}` + '</td><td>' + `${ISSUED}` + '</td><td class="label-cell medium-only">' + `${TITLE}` + '</td><td class="label-cell medium-only">' + `${AUTHOR}` + '</td><td>' + `${TYPE}` + '</td><td>' + `${COPIES}` + '</td><td><i class="icon material-icons button" onclick="titleDetails(' + ACCNO + ',' + LACCDATE + ',' + LISBN + ')">info</i></td>'
}
eel.expose(queryMembersTable)
function queryMembersTable(mode) {
  if (mode == 1) {
    membersTable = $('#query-members').DataTable();
  } else {
    membersTable.destroy(); membersTable.destroy();
  }

}
function memberDetails(UID, NAME, CLASS, ADMID) {
  app.dialog.create({
    title: 'Details',
    text: 'Name : ' + NAME + '. Admission number: ' + ADMID + '. Class: ' + CLASS,
    buttons: [
      {
        text: 'REMOVE',
        onClick: function () { app.progressbar.show(); eel.deleteMember(UID); },
      },
      {
        text: 'OK',
      },
    ],
  }).open();
}
eel.expose(fillMembersHead)
function fillMembersHead() {
  membersTableHead = document.getElementById('query-members-table')
  membersTableHead.innerHTML += '<table id="query-members"><thead class="elevation-1"><tr id="query-members-head"><th class="label-cell">UID</th><th class="label-cell medium-only">NAME</th><th class="label-cell">CLASS</th><th class="label-cell medium-only">EMAIL-ID</th><th class="label-cell">DETAILS</th></tr></thead><tbody id="query-members-body"></tbody></table>'
}
eel.expose(fillMembersBody)
function fillMembersBody(UID, LNAME, TCLASS, EMAILID, ADMID) {
  membersTableBody = document.getElementById('query-members-body')
  NAME = `'${LNAME}'`; LCLASS = `'${TCLASS}'`;
  membersTableBody.innerHTML += '<td class="label-cell">' + `${UID}` + '</td><td class="label-cell medium-only">' + `${LNAME}` + '</td><td class="label-cell">' + `${TCLASS}` + '</td><td class="label-cell medium-only">' + `${EMAILID}` + '</td><td><i class="icon material-icons button" onclick="memberDetails(' + UID + ',' + NAME + ',' + LCLASS + ',' + ADMID + ')">info</i></td>'
}
eel.expose(deleteMemberError)
function deleteMemberError(dMErrNo) {
  if (dMErrNo == 1) {
    delMMsg = "Member has not yet returned some Titles. Submit Title and try again!"
  }
  if (dMErrNo == 2) {
    delMMsg = "Error removing Member - database error occured!"
  }
  app.dialog.create({
    title: 'Details',
    text: delMMsg,
    buttons: [
      {
        text: 'OK',
      },
    ],
  }).open();
  app.progressbar.hide()
}
eel.expose(deleteMemberSuccess)
function deleteMemberSuccess() {
  app.progressbar.hide()
  app.toast.create({
    text: 'Member was successfully removed from records!',
    horizontalPosition: 'center',
    closeTimeout: 4000,
  }).open();
}
eel.expose(deleteTitleError)
function deleteTitleError(dtErrNo) {
  if (dtErrNo == 1) {
    delTMsg = "Title currently in circulation. Please submit title and try again!"
  }
  if (dtErrNo == 2) {
    delTMsg = "Error removing Title - database error occured!"
  }
  app.dialog.create({
    title: 'Error!',
    text: delTMsg,
    buttons: [
      {
        text: 'OK',
      },
    ],
  }).open();
  app.progressbar.hide()
}
eel.expose(deleteTitleSuccess)
function deleteTitleSuccess() {
  app.progressbar.hide()
  app.toast.create({
    text: 'Title was successfully removed from records!',
    horizontalPosition: 'center',
    closeTimeout: 4000,
  }).open();
}
eel.expose(queryReturnsTable)
function queryReturnsTable(mode) {
  if (mode == 1) {
    returnsTable = $('#pending-returns').DataTable();
  } else {
    returnsTable.destroy(); returnsTable.destroy();
  }
}
eel.expose(showLoadingBar)
function showLoadingBar() {
  app.progressbar.show()
}

eel.expose(hideLoadingBar)
function hideLoadingBar() {
  app.progressbar.hide()
}
function returnTitle(ACCNO) {
  app.dialog.create({
    title: 'Submit Title ?',
    buttons: [
      {
        text: 'SUBMIT',
        onClick: function () { app.progressbar.show(); eel.submitTitle(ACCNO); },
      },
      {
        text: 'CANCEL',
      },
    ],
  }).open();
}
eel.expose(fillReturneesHead)
function fillReturneesHead() {
  returneesTableHead = document.getElementById('query-pending-returns-table')
  returneesTableHead.innerHTML += '<table id="pending-returns"><thead class="elevation-1"><tr><th class="label-cell">USER ID</th><th class="label-cell">ACC NUMBER</th><th class="label-cell medium-only">TITLE</th><th class="label-cell medium-only">MEMBER NAME</th><th class="label-cell">CLASS</th><th class="numeric-cell">SUBMIT</th></tr></thead><tbody id="query-pending-returns-body"></tbody></table>'
}
eel.expose(fillReturneesBody)
function fillReturneesBody(UID, ACCNO, TITLE, NAME, CLASS) {
  returneesTableBody = document.getElementById('query-pending-returns-body')
  returneesTableBody.innerHTML += '<td class="label-cell">' + `${UID}` + '</td><td class="label-cell">' + `${ACCNO}` + '</td><td class="label-cell medium-only">' + `${TITLE}` + '</td><td class="label-cell medium-only">' + `${NAME}` + '</td><td class="label-cell">' + `${CLASS}` + '</td><td class="numeric-cell"><i class="icon material-icons button" onclick="returnTitle(' + ACCNO + ')">check</i></td>'
}
eel.expose(submitTitleError)
function submitTitleError(sTErrNo) {
  if (sTErrNo == 1) {
    subTMsg = "Please enter a valid ACCNO"
  }
  if (sTErrNo == 2) {
    subTMsg = "Title doesn't exist in circulation. Please check the details!"
  }
  if (sTErrNo == 3) {
    subTMsg = "Database error from server couln't submit Title!"
  }
  app.progressbar.hide()
  app.dialog.create({
    title: 'Error',
    text: subTMsg,
    buttons: [
      {
        text: 'OK',
      },
    ],
  }).open();
}
eel.expose(submitTitleSuccess)
function submitTitleSuccess() {
  app.progressbar.hide()
  app.toast.create({
    text: 'Submission successful !',
    horizontalPosition: 'center',
    closeTimeout: 4000,
  }).open();
}
function submitadt() {
  app.progressbar.show()
  try {
    addTitleDate.formatValue()
  } catch {
    var today = new Date();
    addTitleDate.setValue([today]);
  }
  LACCDATE = addTitleDate.formatValue()
  LNOC = app.stepper.getValue('.adtnoc')
  addTitleData = app.form.convertToData('#add-title-form');
  if (addTitleData.LACCNO.length !== 0 && addTitleData.LTITLE.length !== 0) {
    eel.submitaddTitleData(addTitleData.LACCNO, addTitleData.LTITLE, addTitleData.LAUTHOR, addTitleData.LISBN, LACCDATE, addTitleData.LTYPE, LNOC)
    document.getElementById("resetadtform").click()
    stepper.setValue(1)
  } else {
    triggeraddTitleDataError()
  }
}
eel.expose(issueTitleError)
function issueTitleError(iTErrNo) {
  switch (iTErrNo) {
    case 1: iTMsg = "Please enter the required values properly!"
      break;
    case 2: iTMsg = "Error Title not found. Please check the details!"
      break;
    case 3: iTMsg = "Error Member not found. Please check the details!"
      break;
    case 4: iTMsg = "The title is already in Circulation! Cannot issue unitl returned!"
      break;
    case 5: iTMsg = "The Member is already in Circulation! Cannot issue unitl returned!"
      break;
    case 6: iTMsg = "Database error from server couln't issue Title!"
      break;
    default: iTMsg = "Unknown error occured please check values!"
  }
  app.progressbar.hide()
  app.dialog.create({
    title: 'Error',
    text: iTMsg,
    buttons: [
      {
        text: 'OK',
      },
    ],
  }).open();
}
eel.expose(issueTitleSuccess)
function issueTitleSuccess() {
  app.progressbar.hide()
  app.toast.create({
    text: 'Issue successful !',
    horizontalPosition: 'center',
    closeTimeout: 4000,
  }).open();
}
// Issue Title
$$('.issue-title').on('click', function () {
  app.dialog.login("Enter UID and ACCNO", 'Issue a Title', function (username, password) {
    app.progressbar.show();
    if (username.length !== 0 && password.length !== 0) {
      eel.issueTitle(username, password);
    } else {
      issueTitleError(1);
    }
  });
})
// Return Title
$$('.return-title').on('click', function () {
  app.dialog.password("Enter ACCNO", 'Return Title', function (password) {
    if (password.length !== 0) {
      eel.submitTitle(password);
    } else { submitTitleError(1) }
  });
});
var stepper = app.stepper.get('.stepper');
function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('timeDisplayH').innerHTML =
    h + ":" + m + ":" + s;
  document.getElementById('timeDisplayR').innerHTML =
    h + ":" + m + ":" + s;
  document.getElementById('timeDisplayC').innerHTML =
    h + ":" + m + ":" + s;
  var t = setTimeout(startTime, 500);
}
function checkTime(i) {
  if (i < 10) { i = "0" + i };
  return i;
}
eel.expose(triggerChangeSuccess)
function triggerChangeSuccess(tT, tC, lM) {
  document.getElementById("libT").innerText = "Total Titles : " + `${tT}`
  document.getElementById("libC").innerText = "Total Copies : " + `${tC}`
  document.getElementById("libM").innerText = "Library Members : " + `${lM}`
}
