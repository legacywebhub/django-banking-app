'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
'Content-Type': 'multipart/form-data',
'Process-Data': false,

const getFormData = object => Object.keys(object).reduce((formData, key) => {
    formData.append(key, object[key]);
    return formData;
}, new FormData());