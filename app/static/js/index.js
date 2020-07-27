data = [[,]];
sheet = jexcel(document.getElementById('spreadsheet'), {
  minDimensions:[2,2],
  wordWrap:true,
});

const request_impute = async () => {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", '/request_impute', true);

  xhr.send(JSON.stringify(sheet.getData()));
}
const imputeButton = document.getElementById('imputeButton')
imputeButton.onclick = () => {
  request_impute();
}