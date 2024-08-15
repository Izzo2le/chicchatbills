from django.db import models

class User(models.Model):
    UID = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    listOfBills = models.ManyToManyField('Bill', blank=True)

    def updateBills(self, newListOfBills):
        self.listOfBills.set(newListOfBills)

    def addNewBill(self, bill):
        self.listOfBills.add(bill)

    def deleteABill(self, UID):
        self.listOfBills = self.listOfBills.exclude(UID=UID)

class Bill(models.Model):
    UID = models.AutoField(primary_key=True)
    listOfItems = models.ManyToManyField('Item', blank=True)

    def addNewItemToBill(self, item):
        self.listOfItems.add(item)

    def removeItemFromBill(self, UID):
        self.listOfItems = self.listOfItems.exclude(UID=UID)

class Item(models.Model):
    UID = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    description = models.TextField()
    numberOfSplits = models.IntegerField()
    BillId = models.ForeignKey(Bill, on_delete=models.CASCADE)
    pricePerSplit = models.DecimalField(max_digits=10, decimal_places=2)

    def updateNumberOfSplits(self, newNumberOfSplits):
        self.numberOfSplits = newNumberOfSplits
        self.pricePerSplit = self.price / newNumberOfSplits

    def renameItem(self, newName):
        self.name = newName

    def renameDescription(self, newDescription):
        self.description = newDescription

