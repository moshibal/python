const bishal = {
  firstName: "Bishal",
  lastName: "Karki",
  birthyear: 1995,
  job: "web developer",
  friends: ["Micheal", "Peter", "Bimash"],
  hasDriversLicense: true,
  calAge: function () {
    this.age = 2023 - this.birthyear;
    return this.age;
  },
  describtion: function () {
    return `${this.firstName} is a ${this.calAge()}-year old ${
      this.job
    }, and he has ${this.hasDriversLicense ? "a" : "no"} driver's license.`;
  },
};
console.log(bishal.describtion());
