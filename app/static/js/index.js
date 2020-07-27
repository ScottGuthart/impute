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
        // sheet.setData(this.response)
        console.log(this.response)
        check_task_result(this.response)
    }
}

  xhr.send(JSON.stringify(data));
}
const imputeButton = document.getElementById('imputeButton')
imputeButton.onclick = () => {
  var data = sheet.getData();
  request_impute(data);
}

const check_task_result = async (task_id) => {
  fetch('/check_task_result/'+task_id)
  .then(response=>response.json())
  .then(data => {
    if (data.length > 1) {
      sheet.setData(data)
    }
    else {
      console.log(`Progress: ${data}`)
      setTimeout(function() {
        check_task_result(task_id);
      }, 2000);
    }
  })
  var oReq = new XMLHttpRequest();
  oReq.onload = function() {
    console.log(JSON.stringify(oReq.response))
  }
  oReq.open("GET", `/check_task_result/${task_id}`, true);
}