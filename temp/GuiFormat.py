{type:"window",Align:"V",data:[
	{type:"frame",Align:"H",data:[
		{type:"Button",w:200,h:40,text="Start",cmd=func},
		{type:"Button",w:200,h:40,text="Midls",cmd=func},
		{type:"Button",w:200,h:40,text="DoneR",cmd=func}
		]
	},
	{type:"frame",Align:"H",data:[
		{type:"TreeView",w:200,h:-1,cmd=func},
		{type:"ListView",w:-1 ,h:-1,cmd=func}
		]
	},
	{type:"ToolBar",Align:"H",data:[
		{type:"Label",w:200,h:-1,cmd=func},
		{type:"Edits",w:-1 ,h:-1,cmd=func}
		]
	}
	]
}
<?TPP version=1>
	<window id=0x100 align="V">
		<frame align="H">
			<Button w=200 h=40 cmd=func>Start</Button>
			<Button w=200 h=40 cmd=func>Midls</Button>
			<Button w=200 h=40 cmd=func>DoneR</Button>
		</frame>
		<frame align="H">
			<TreeView id=0x011 w=200 h=-1 cmd=func></TreeView>
			<ListView id=0x012 w=-1  h=-1 cmd=func></ListView>
		</frame>
		<ToolBar align="H">
			<Label w=200 h=-1 cmd=func>files</Label>
			<Edits w=-1  h=-1 cmd=func>views</Edits>
		</ToolBar>
	</window>
</TPP>
