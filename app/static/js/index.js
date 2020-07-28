var wait = 0;
data = [[,]];
sheet = jexcel(document.getElementById('spreadsheet'), {
  minDimensions:[2,2],
  wordWrap:true,
  onbeforepaste: (instance, data, x, y) => {
    jSuites.loading.show();
    return data
  },
  onpaste: () => {
    jSuites.loading.hide();
  }
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
  if (imputeButton.textContent.includes('Impute')){
    var data = sheet.getData();
    request_impute(data);
  }
}

const check_task_result = async (task_id) => {
  fetch('/check_task_result/'+task_id)
  .then(response=>response.json())
  .then(data => {
    if (data.length > 1) {
      sheet.setData(data)
      imputeButton.textContent = 'Impute'
      wait = 0;
    }
    else if (typeof(data[0]) == "string" && data[0].includes('ERROR')) {
      alert(data[0]);
      imputeButton.textContent = 'Impute'
      wait = 0;
    }
    else if (wait >= 100) {
      alert('Impute timed out. Maybe try again in a bit? Or let Scott know')
      imputeButton.textContent = 'Impute'
      wait = 0;
    }
    else {
      console.log(`Progress: ${data} wait: ${wait}`)
      imputeButton.textContent = `${wait}%`
      wait += 5;
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