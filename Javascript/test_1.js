'use strict';

function Fruit (type) {
    this.type = type;
    this.color = 'unknown';
    this.country = 'unknown';
    this.getInformation = function(){
        return "This " + this.type + " is " + this.color + " and comes from " + this.country;
    }
}

class OlivetGroup {
    constructor(name, CEO, employees){
        this.name = name;
        this.CEO = CEO; 
        this.employees = employees;
    }
    report_CEO(){
        console.log(this.name + '\'s CEO is ' + this.CEO);
    }
    report_employees(){
        var employee_list = '';
        for (let x of this.employees){
            if(x == this.CEO){
                continue;
            }
            else{
                employee_list += x + ', ';
            }
        }
        console.log(this.name + '\'s employees are ' + employee_list);
    }

}

class Crossmap extends OlivetGroup{
    constructor(CEO, employees){
        super(CEO, employees);
        this.name = "Crossmap";
    }

} 


let lime = new Fruit('Mexican lime');
console.log(lime.getInformation());

lime.color = 'green';
lime.country = 'China';
console.log(lime.getInformation());
let Crossmap1 = new OlivetGroup('Crossmap', 'Lee Sanggi', ['Lee Sanggi', 'Shin Bohwa', 'Choi Hyungsuk', 'Yang Moonjeong', 'Koo Jeonghwa', 'Jeong Jihoon', 'Jun Minsu', 'Jeong Hwi', 'Lee Jaemin', 'Do Sangtae', 'Jang Jidong']);
console.log(Crossmap1);
Crossmap1.report_CEO();
Crossmap1.report_employees();
let Crossmap2 = new Crossmap('Lee Sanggi', ['Lee Sanggi', 'Shin Bohwa', 'Choi Hyungsuk', 'Yang Moonjeong', 'Koo Jeonghwa', 'Jeong Jihoon', 'Jun Minsu', 'Jeong Hwi', 'Lee Jaemin', 'Do Sangtae', 'Jang Jidong']);
console.log(Crossmap2);
Crossmap2.report_CEO;
Crossmap2.report_employees();



