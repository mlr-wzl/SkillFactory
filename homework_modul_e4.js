// JavaScript source code

// Task 1
function getObject(object) {
    for (let key in object) {
        if (object.hasOwnProperty(key)) {
            console.log(key +";"+ object[key]);
        }
    }
}
const person = {

    city: "Moscow"

}

const student = Object.create(person);

student.ownCity = "Piter";

getObject(student)

//Task 2
function proveObject(object, string) {
    for (let key in object) {
        if (key == string) {
            return true;
        }
    }
    return false 
    }

proveObject(student, "city")

//Task 3
function createEmptyObject() {  
    return object=Object.create(null);
}

// Task 4
function ElectricalDevice(name,power) {
    this.name = name;
    this.plugged = false;
    this.power = power;

}

ElectricalDevice.prototype.plugIn = function () {
    this.plugged = true;
}

ElectricalDevice.prototype.plugOut = function () {
    this.plugged = false;
}

function ElectricalDisplay(volume) {
    this.volume = volume;
}

function ElectricalTouchDisplay() {
    this.touch = true;
}

ElectricalDisplay.prototype = new ElectricalDevice()
ElectricalTouchDisplay.prototype = new ElectricalDisplay()

ElectricalDisplay.prototype.light = function () {
    console.log("Display lightens");
}

ElectricalTouchDisplay.prototype.light = function () {
    console.log("Touch Display lightens");
}

const TouchDisplay = new ElectricalTouchDisplay("Dell", 2, 4)
const NoTouchDisplay = new ElectricalDisplay("Philips", 3, 4)
console.log(TouchDisplay.plugged)
TouchDisplay.plugIn()
console.log(TouchDisplay.plugged)

//Task 5
class ElectricalDevice {
    constructor(name, power){
        this.name = name;
        this.plugged = false;
        this.power = power;
    }
    plugIn () {
        this.plugged = true;
    }
    plugOut () {
        this.plugged = false;
    }
}


class ElectricalDisplay extends ElectricalDevice {
    constructor(volume,name,power) {
        super(name,power);
        this.volume = volume;
    }

    light() {
        console.log("Display lightens");
    }
}

class ElectricalTouchDisplay extends ElectricalDisplay{
    constructor(volume, name, power) {
        super(name,power,volume);
        this.touch = true;
    }
    light() {
        console.log("Touch Display lightens");
    }
}

const TouchDisplay1 = new ElectricalTouchDisplay("Dell", 2, 3)
const NoTouchDisplay1 = new ElectricalDisplay("Philips", 3, 4)
console.log(TouchDisplay1.plugged)
TouchDisplay1.plugIn()
console.log(TouchDisplay1.plugged)
TouchDisplay1.light()
NoTouchDisplay1.light()
