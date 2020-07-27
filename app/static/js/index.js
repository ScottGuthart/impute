data = [[,]];
sheet = jexcel(document.getElementById('spreadsheet'), {
  minDimensions:[2,2],
  wordWrap:true,
});

const request_impute = async (data) => {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", '/request_impute', true);
  xhr.onreadystatechange = function() { // Call a function when the state changes.
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        // Request finished. Do processing here.
        sheet.setData(this.response)
    }
}

  xhr.send(JSON.stringify(data));
}
const imputeButton = document.getElementById('imputeButton')
imputeButton.onclick = () => {
  var data = sheet.getData();
  request_impute(data);
}