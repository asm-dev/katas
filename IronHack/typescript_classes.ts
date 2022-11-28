// Create an Employee class to represent an employee of a company. Add all relevant properties and behaviors that you might need but you have to include a salary property. Don’t forget to add getters and setters.

class Employee {
    constructor (
        private _name : string,
        private _startDate: Date,
        private _salary: number,
    ){};

    set name(name:string) {
        this._name = name;
    }

    get name():string {
        return this._name;
    }

    set startDate(startDate: Date){
        this._startDate = startDate;
    }
    get startDate(): Date{
        return this._startDate;
    }

    set salary(salary:number){
        this._salary = salary;
    }
    get salary():number{
        return this._salary;
    }
}

// Create an Intern class that extends from Employee. All the Interns have a salary limit of 20000 (constant). You must validate if an intern is created (or salary updated) with a bigger salary than the max. The max value is set.

class Intern extends Employee {
    constructor (
        name : string,
        startDate: Date,
        salary: number,
    ) {
        super(name, startDate, salary);
        this.salary = salary
    }

    set salary(salary:number) {
        if (salary > 20000) {
            super.salary = 20000;
        } else {
            super.salary = salary
        }
    }
}

let employee: Employee = new Employee (
    "Ana",
    new Date("2022, 11, 29"), // Syntax: new Date(year, monthIndex, day)
    35000,
)

let intern: Intern = new Intern (
    "Becaria",
    new Date("2022, 11, 31"),
    25000,
)

console.log(employee);
console.log(intern);