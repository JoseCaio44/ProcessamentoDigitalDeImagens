<?xml version="1.0" encoding="ISO-8859-1"?>
<ncl id="exemplo01" xmlns="http://www.ncl.org.br/NCL3.0/EDTVProfile">
<head>
<regionBase>
<region id="rgTV">
<region id="rgVideo1" zIndex="1" />
<region id="rgImag1" left="5%" top="5%" width="10%" height="10%"  zIndex="4"/>
</region>
</regionBase>
<descriptorBase>
	<descriptor id="dVideo1" region="rgVideo1"/>
	<descriptor id="dImag1" region="rgImag1" />
</descriptorBase>
<connectorBase>
<causalConnector id="onBeginStart">
<simpleCondition role="onBegin"/>
<simpleAction role="start"/>
</causalConnector>
<causalConnector id="onEndStop">
<simpleCondition role="onEnd"/>
<simpleAction role="stop"/>
</causalConnector>

<causalConnector id="onKeySelectionStop">
	<connectorParam name="aKey" />
	<simpleCondition role="onSelection" key="$aKey" />
	<simpleAction role="stop" />
</causalConnector>

<causalConnector id="onEndStart">
	<simpleCondition role="onEnd"/>
	<simpleAction role="start" />
</causalConnector>

</connectorBase>
</head>
<body>
<port id="pVideoAbertura" component="VideoAbertura" />
<media id="VideoAbertura" src="mj.mp4" descriptor="dVideo1" />
<media id="imagPularIntro" src="logo.png" descriptor="dImag1" />
<media id="VideoPrincipal" src="piu.mp4" descriptor="dVideo1" />

<link xconnector="onBeginStart">
<bind component="VideoAbertura" role="onBegin" />
<bind component="imagPularIntro" role="start" />
</link>
<link xconnector="onEndStop">
<bind component="VideoAbertura" role="onEnd" />
<bind component="imagPularIntro" role="stop" />
</link>

<link xconnector="onKeySelectionStop">
	<bind component="imagPularIntro" role="onSelection">
		<bindParam name="aKey" value="GREEN" />
	</bind>
	<bind component="VideoAbertura" role="stop" />
</link>

<link xconnector="onEndStart">
	<bind component="VideoAbertura" role="onEnd"/>
	<bind component="VideoPrincipal" role="start"/>
</link>

</body>
</ncl>