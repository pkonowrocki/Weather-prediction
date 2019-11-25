naturalCode = {
    'Calm, no wind' : '0;0;0;0',
    'Wind blowing from the north' : '1;0;0;0',
    'Wind blowing from the south' : '0;0;0;1',
    'Wind blowing from the east' : '0;1;0;0',
    'Wind blowing from the west' : '0;0;1;0',
    'Wind blowing from the north-west' : '0.5;0;0.5;0',
    'Wind blowing from the north-east' : '0.5;0.5;0;0',
    'Wind blowing from the south-west' : '0;0;0.5;0.5',
    'Wind blowing from the south-east' : '0;0.5;0;0.5',
    'Wind blowing from the north-northwest' : '0.667;0;0.333;0',
    'Wind blowing from the north-northeast' : '0.667;0.333;0;0',
    'Wind blowing from the east-northeast' : '0.333;0.667;0;0',
    'Wind blowing from the east-southeast' : '0;0.667;0;0.333',
    'Wind blowing from the south-southeast' : '0;0.333;0;0.667',
    'Wind blowing from the south-southwest' : '0;0;0.333;0.667',
    'Wind blowing from the west-southwest' : '0;0;0.667;0.333',
    'Wind blowing from the west-northwest' : '0.333;0;0.667;0',
}

grayCode = {
    'Calm, no wind' : '0;0;0;0;0',
    'Wind blowing from the north' : '0;0;0;0;1',
    'Wind blowing from the north-northeast' : '0;0;0;1;1',
    'Wind blowing from the north-east' : '0;0;0;1;0',
    'Wind blowing from the east-northeast' : '0;0;1;1;1',
    'Wind blowing from the east' : '0;0;1;0;1',
    'Wind blowing from the east-southeast' : '0;0;1;0;0',
    'Wind blowing from the south-east' : '0;1;1;0;0',
    'Wind blowing from the south-southeast' : '0;1;1;0;1',
    'Wind blowing from the south' : '0;1;1;1;1',
    'Wind blowing from the south-southwest' : '0;1;1;1;0',
    'Wind blowing from the south-west' : '0;1;0;1;0',
    'Wind blowing from the west-southwest' : '0;1;0;1;1',
    'Wind blowing from the west' : '0;1;0;0;1',
    'Wind blowing from the west-northwest' : '0;1;0;0;0',
    'Wind blowing from the north-west' : '1;1;0;0;0',
    'Wind blowing from the north-northwest' : '1;1;0;0;1',
}

cloudsOktaCode = {
    'no clouds' : '0',
    'Sky obscured by fog and/or other meteorological phenomena.' : '9',
    '90  or more, but not 100%' : '7',
    '70  80%.' : '6',
    '60%.' : '5',
    '50%.' : '4',
    '40%.' : '3',
    '2030%.' : '2',
    '100%.' : '8',
    '10%  or less, but not 0' : '1'
}

cloudsOktaGrayCode = {
    'no clouds' : '0;0;0;0',
    '10%  or less, but not 0' : '0;0;0;1',
    '2030%.' : '0;0;1;1',
    '40%.' : '0;0;1;0',
    '50%.' : '0;1;1;0',
    '60%.' : '0;1;1;1',
    '70  80%.' : '0;1;0;1',
    '90  or more, but not 100%' : '0;1;0;0',
    '100%.' : '1;1;0;0',
    'Sky obscured by fog and/or other meteorological phenomena.' : '1;1;0;1'
}

cloudsOktaStupidCode = {
    'no clouds' : '0;0;0;0;0;0;0;0;0;1',
    '10%  or less, but not 0' : '0;0;0;0;0;0;0;0;1;0',
    '2030%.' : '0;0;0;0;0;0;0;1;0;0',
    '40%.' : '0;0;0;0;0;0;1;0;0;0',
    '50%.' : '0;0;0;0;0;1;0;0;0;0',
    '60%.' : '0;0;0;0;1;0;0;0;0;0',
    '70  80%.' : '0;0;0;1;0;0;0;0;0;0',
    '90  or more, but not 100%' : '0;0;1;0;0;0;0;0;0;0',
    '100%.' : '0;1;0;0;0;0;0;0;0;0',
    'Sky obscured by fog and/or other meteorological phenomena.' : '1;0;0;0;0;0;0;0;0;0',
}