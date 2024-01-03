const tagInput = document.querySelector(".tag-input");
const tagArea = document.querySelector(".tag-area");
const ul = document.querySelector(".tag-area ul");
const visualContainer = document.querySelector("#visual-container");
const size = document.querySelector("#size");
const generateRand = document.querySelector("#generate-rand");
const typeManually = document.querySelector("#type-manual");
const sizeNumber = document.querySelector("#size-number");
const manualBox = document.querySelector("#manual-box");
const startBtn = document.querySelector("#start-btn");
let step = 0;
let mainArr = [];
// handles manually typing the numbers
let manuallyTyped = [];
size.addEventListener("change", (e) => {
  sizeNumber.textContent = "size of " + e.target.value;
  if(manuallyTyped.length !== +e.target.value){
    startBtn.classList.add('hidden');
  }
  else {
    startBtn.classList.remove('hidden')
  }

});
window.onload = () => {
  sizeNumber.textContent = "size of " + size.value;
};
function addEvent(element) {
  tagArea.addEventListener("click", () => {
    element.focus();
  });

  element.addEventListener("focus", () => {
    tagArea.classList.add("active");
  });
  if (element instanceof HTMLInputElement) {
    element.addEventListener("change", (e) => {
      if (isNaN(+e.target.value)) {
        return;
      } else {
        element.value = e.target.value;
      }
    });
  }
  element.addEventListener("blur", (e) => {
    tagArea.classList.remove("active");

    if (element.value.match(/^[0-9]+$/gi) && element.value !== "") {
      manuallyTyped.push(e.target.value.trim());
      if(manuallyTyped.length === +size.value ){
        startBtn.classList.remove('hidden');
      }
      element.value = "";
      renderTags();
    } else {
      element.value = "";
    }
  });

  element.addEventListener("keydown", (e) => {
    const value = e.target.value;
    if (
      (e.keyCode === 32 ||
        e.keyCode === 13 ||
        value[value.length - 1] === " ") &&
      value.match(/^[0-9]+$/gi) &&
      value !== "" &&
      manuallyTyped.length < +size.value
    ) {
      manuallyTyped.push(e.target.value.trim());
      element.value = "";
      renderTags();
    }
    if (e.keyCode === 8 && value === "") {
        manuallyTyped.pop();
        startBtn.classList.add('hidden');
        renderTags();
    }
    if(manuallyTyped.length === +size.value){
      startBtn.classList.remove('hidden');
    }
  });
}
addEvent(tagInput);

function renderTags() {
  ul.innerHTML = "";
  manuallyTyped.forEach((tag, index) => {
    createTag(tag, index);
  });
  const input = document.createElement("input");
  input.type = "text";
  input.className = "tag-input";
  addEvent(input);
  ul.appendChild(input);
  input.focus();
  setTimeout(() => (input.value = ""), 0);
}
typeManually.addEventListener("click", () => {
  if (manuallyTyped.length === 0 && !manualBox.classList.contains("hidden")) {
    generateRand.disabled = false;
  } else {
    generateRand.disabled = true;
  }
  manualBox.classList.toggle("hidden");
});

function createTag(tag, index) {
  const li = document.createElement("li");
  li.className = "tag";
  const text = document.createTextNode(tag);
  const cross = document.createElement("span");
  cross.className = "cross";
  cross.dataset.index = index;
  cross.addEventListener("click", (e) => {
    manuallyTyped = manuallyTyped.filter(
      (_, index) => index != e.target.dataset.index
    );
    startBtn.classList.add('hidden');
    renderTags();
  });
  li.appendChild(text);
  li.appendChild(cross);
  ul.appendChild(li);
}

// handles generating array

function createArrBlocks({
  heading = "",
  arr = [],
  index = -1,
  reason = "",
  smallIndex = -2,
  bigIndex = -3,
  currElm,
}) {
  const ArrContainer = document.createElement("div");
  ArrContainer.className = "arr-container";
  if (heading !== "") {
    let h2 = document.createElement("h2");
    h2.textContent = heading;
    visualContainer.appendChild(h2);
  }
  arr.forEach((elm, arrIndex) => {
    const elmBlock = document.createElement("div");
    elmBlock.textContent = elm;
    if (arrIndex === smallIndex) {
      elmBlock.className = "small-index";
    }
    if (arrIndex === bigIndex) {
      elmBlock.className = "big-index";
    }
    if (step === mainArr.length - 1) {
      elmBlock.className = "final-result";
    }
    if (arrIndex === currElm?.prev || arrIndex === currElm?.next) {
      elmBlock.className = "curr-index";
    }
    elmBlock.dataset.index = index;
    ArrContainer.appendChild(elmBlock);
  });
  // this is for the initial array
  if (index === -1) {
    visualContainer.appendChild(ArrContainer);
    return;
  }
  const IndexContainer = document.createElement("div");
  IndexContainer.className = "index-container";
  const Index = document.createElement("p");
  Index.textContent = `J = ${index}`;
  IndexContainer.appendChild(Index);
  if (reason) {
    const reasonContainer = document.createElement("div");
    reasonContainer.className = "reason-container";
    const reasonElm = document.createElement("p");
    reasonElm.textContent = reason;
    reasonContainer.appendChild(ArrContainer);
    reasonContainer.appendChild(reasonElm);
    IndexContainer.appendChild(reasonContainer);
    visualContainer.appendChild(IndexContainer);
    return;
  }
  IndexContainer.appendChild(ArrContainer);
  visualContainer.appendChild(IndexContainer);
}

// bubble sorter
function bubbleSort(arr, stop) {
  for (let i = step; i < arr.length; i++) {
    let h2 = document.createElement("h2");
    h2.textContent = `Step ${i}`;
    visualContainer.appendChild(h2);
    for (let j = 0; j < arr.length - i - 1; j++) {
      let bigIndex,
        smallIndex,
        reason = "";
      // swap elements
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        reason = `We Swapped ${arr[j]} with ${arr[j + 1]} because ${
          arr[j + 1]
        } is a bigger number.`;
        bigIndex = j + 1;
        smallIndex = j;
      }
      if (reason === "") {
        reason = `We kept the array the same because ${arr[j]} is ${
          arr[j] === arr[j + 1] ? "equal to " : "less than"
        } ${arr[j + 1]}`;
      }
      createArrBlocks({
        arr: mainArr,
        bigIndex,
        smallIndex,
        currElm: {
          prev: smallIndex ? undefined : j,
          next: bigIndex ? undefined : j + 1,
        },
        reason,
        index: j,
      });
    }
    step += 1;
    if (stop) {
      createNextBtn();
      break;
    }
  }
}
// create btn 
function createBtn({
    text = "",
    className = "next-button",
    handler = () => void 0,
    parentContainer = visualContainer
}){
    const btnContainer = document.createElement("div");
    btnContainer.className = "button-container";
    const btn = document.createElement("button");
    btn.textContent = text;
    btn.className = className;
    btnContainer.appendChild(btn);
    parentContainer.appendChild(btnContainer);
    btn.addEventListener("click", handler);
}
// create next button
function createNextBtn() {
  if (step < mainArr.length - 1) {
  new createBtn({
        text : "Next Step",
        handler () {
        visualContainer.removeChild(visualContainer.lastChild);
      bubbleSort(mainArr, true); 
        }
    })
  } else {
    createArrBlocks({
      heading: "final result",
      arr: mainArr,
    });
    createResetBtn() 
  }
}

function createResetBtn(){
    createBtn({
        text: "Reset",
        handler(){
            mainArr.length = 0;
            step = 0;
            manuallyTyped.length = 0;
            generateRand.disabled = false;
            typeManually.disabled = false;
            ul.innerHTML = '';
            ul.appendChild(tagInput);
            let firstChild = visualContainer.firstChild;
            while(firstChild){
                visualContainer.removeChild(firstChild);
                firstChild = visualContainer.firstChild
            }
        }
    })
}
// generate random arr
function generateRandomArr() {
  for (let i = 0; i < size.value; i++) {
    mainArr.push(Math.floor(Math.random() * 100));
  }
  createArrBlocks({
    heading: "Initial Array",
    arr: mainArr,
  });
  createNextBtn();
}
// generate manual arr
function generateManualArr() {
    // creates a copy of manually typed array and converts its contents to a number.
    mainArr = manuallyTyped.slice().map((item) => +item);
    createArrBlocks({
        heading: "Initial Array",
        arr: mainArr,
      });
      createNextBtn();
}
generateRand.addEventListener("click", () => {
  typeManually.disabled = true;
  generateRand.disabled = true;
  generateRandomArr();
});
startBtn.addEventListener("click", () => {
    typeManually.disabled = true;
  generateRand.disabled = true;
  manualBox.classList.add('hidden');
  startBtn.classList.add('hidden');
  generateManualArr();
})