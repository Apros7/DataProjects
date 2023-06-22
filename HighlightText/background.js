chrome.runtime.onInstalled.addListener(function() {
    chrome.contextMenus.create({
        "title": 'Magic button',
        "contexts": ["selection"],
        "id": "myContextMenuId"
    });
  });

    
chrome.contextMenus.onClicked.addListener(function(info, tab) {
    let text = info.selectionText
    document.body.innerHTML = `<h3>${text}</h3>`
  })