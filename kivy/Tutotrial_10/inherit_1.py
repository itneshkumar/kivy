# inherit the color properties

<Button>
    #font_size: 50
    background_normal: ""
    background_color: (0,0,1,1)
<Inputbox>
    background_color: (250/255,2/250,0,1)
<Label>
    font_size:32 # here upper most button font size has commented stil you find the same size of the label font size of button, its override

<MyLayout>
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        paddinng: 10
        spacing: 10

        Label:
            text: "Name"
        TextInput:
            multiline: False
        Label:
            text: "Favorite Pizza"
        TextInput:
            multiline: False
        Button:
            text: "submit"
        Button:
            text: "clear"
        Button:
            text: "submit"
            background_color: (1,0,0,1)