'''

The following util software extracts the information from the Portland Housing Burero State of Housing
data sheets.  A Template is built and each neighboorhood sheet is extracted with that template definition

'''
import xlrd
import xlrd.sheet
from neighboorhood_template import getNeighboorhoodField

inpfile = '../SoH/Neighborhood Profiles Datasheet.xlsx'


def buildNeihboorhoodProfiles():
    workbook = xlrd.open_workbook(inpfile)
    print (inpfile)
    neighboorlist = []
    for sheet in workbook.sheets():
        idx = 0
        r, c, field, idx = getNeighboorhoodField(idx)
        neighboor_fields = {}
        neighboor_fields ['neighboorhood'] = sheet.name
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                if row == r and col == c:
                    neighboor_fields[field] = sheet.cell(r,c).value
                    r, c, field, idx = getNeighboorhoodField(idx)
                    if r < 0:
                        neighboorlist.append(neighboor_fields)
                        break
    return neighboorlist
        
def buildNeihboorhoodInsert(lst):
    keystr = '('
    valuestr = '('
    keycnt = 0
    keylen = len(lst.keys())
    for k in lst.keys():
        keycnt = keycnt + 1
        if lst[k] != '':
            keystr = keystr + k
            valuestr = valuestr + str(lst[k])
            if keycnt < (keylen - 1):
                keystr = keystr + ','
                valuestr = valuestr + ','
    keystr = keystr +  ')'
    valuestr = valuestr  +')'
    return keystr, valuestr
        
def loadNeihboorhoodProfiles(neighboorlist, debug):
    for l in neighboorlist:
        keystr, valuestr = buildNeihboorhoodInsert(l)

        '''
        Place SQL code where we insert fields from keystr with values from valuestr
        '''
        if debug == True:
            print (l['neighboorhood'])
            print (keystr)
            print (' ')
            print (valuestr)
            print (' ')
        
def main():
    neighboorlist = buildNeihboorhoodProfiles()
    loadNeihboorhoodProfiles(neighboorlist, True)
if __name__ == '__main__':
    main()