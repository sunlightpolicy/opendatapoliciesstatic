function onSubmit(e) {
  
  var response = e.response;
  var itemResponses = response.getItemResponses();
  
  // Create object where: keys = item titles, values = item answers
  var answers = {};
  for (var i = 0; i < itemResponses.length; i++) {
    var ir = itemResponses[i];
    var title = ir.getItem().getTitle();
    var answer = ir.getResponse();
    answers[title] = answer;
  }
  
  var recipient = answers['Email'];
  Logger.log(recipient);
  
  Logger.log(answers['Date']);
  Logger.log(typeof answers['Date']);
  if (answers['Date'].length > 0) {
    var date_obj = new Date(answers['Date'].replace('-', '/') + '/' + answers['Year']);
    Logger.log('date_obj:');
    Logger.log(date_obj);
    var date = date_obj.toISOString().substr(0,10);
  } else {
    var date = '';
  }
  Logger.log(date);
  var geo = Maps.newGeocoder().geocode(answers['Place name'].trim() + ', ' + answers['State']);
  Logger.log(typeof geo);
  Logger.log(geo);
  var x = geo.results[0].geometry.location.lng;
  var y = geo.results[0].geometry.location.lat;
  Logger.log(x);
  Logger.log(y);
  var wwc = answers['WWC'].replace('Yes', 'true').replace('No', 'false');
  var place = answers['Place name'].trim().toLowerCase().replace(/ /g, '-') + '-' + answers['State'].toLowerCase();
  Logger.log(place);

  var emailString = ('Here is the information. (This is an auto-generated email.)\n\n' +
                     (answers['Notes'] ? ('\nNotes:\n' + answers['Notes']) : '') + '\n\n##Potential new place to be added:\n\n' +
                     '---\nplace: ' + place + '\ntitle: ' + answers['Place name'].trim() + '\nstates:\n  - ' + answers['State'] +
                     '\ntype: local' + '\nx: ' + x + '\ny: ' + y + '\nwwc: ' + wwc + '\n---\n\n##New policy to be added:\n\n' +
                     '---\nplace: ' + place + '\nyear: ' + answers['Year'] + '\ndate: ' + date + '\nlegal_custom: ' + answers['Legal Means'] +
                     '\npolicy_url: ' + answers['URL'] + '\n---\n\n' + answers['Text'].replace('\n\n', '\n') + '\n');
  
  Logger.log(1);
  GmailApp.sendEmail(recipient,
                     "Thank you for submitting a new policy",
                     emailString);
  Logger.log(2);
  GmailApp.sendEmail("gjordandetamore@sunlightfoundation.com",
                     "New policy submitted",
                     emailString);
  Logger.log(3);
}
