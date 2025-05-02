{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 6,
			"revision" : 5,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 58.0, 94.0, 1031.0, 681.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"assistshowspatchername" : 0,
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 266.0, 550.0, 104.0, 22.0 ],
					"text" : "prepend influence"
				}

			}
, 			{
				"box" : 				{
					"bgmode" : 0,
					"border" : 0,
					"clickthrough" : 0,
					"enablehscroll" : 0,
					"enablevscroll" : 0,
					"id" : "obj-26",
					"lockeddragscroll" : 0,
					"lockedsize" : 0,
					"maxclass" : "bpatcher",
					"name" : "somax.audioinfluencer.app.maxpat",
					"numinlets" : 1,
					"numoutlets" : 5,
					"offset" : [ 0.0, 0.0 ],
					"outlettype" : [ "", "multichannelsignal", "", "", "" ],
					"patching_rect" : [ 16.0, 135.0, 274.0, 329.0 ],
					"varname" : "somax.audioinfluencer.app",
					"viewvisibility" : 1
				}

			}
, 			{
				"box" : 				{
					"bgmode" : 0,
					"border" : 0,
					"clickthrough" : 0,
					"enablehscroll" : 0,
					"enablevscroll" : 0,
					"id" : "obj-25",
					"lockeddragscroll" : 0,
					"lockedsize" : 0,
					"maxclass" : "bpatcher",
					"name" : "somax.player.app.maxpat",
					"numinlets" : 2,
					"numoutlets" : 5,
					"offset" : [ 0.0, 0.0 ],
					"outlettype" : [ "multichannelsignal", "", "", "", "" ],
					"patching_rect" : [ 530.0, 646.0, 294.0, 864.0 ],
					"varname" : "somax.player.app",
					"viewvisibility" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "signal" ],
					"patching_rect" : [ 169.0, 59.0, 35.0, 22.0 ],
					"text" : "adc~"
				}

			}
, 			{
				"box" : 				{
					"bubble" : 1,
					"id" : "obj-51",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 733.0, 1653.0, 77.166666666666686, 24.0 ],
					"saved_attribute_attributes" : 					{
						"bubble_bgcolor" : 						{
							"expression" : "themecolor.theme_bubble_bgcolor"
						}
,
						"textcolor" : 						{
							"expression" : "themecolor.theme_textcolor"
						}

					}
,
					"text" : "start dsp"
				}

			}
, 			{
				"box" : 				{
					"checkedcolor" : [ 0.482352941176471, 0.847058823529412, 0.36078431372549, 1.0 ],
					"id" : "obj-145",
					"ignoreclick" : 1,
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 739.0, 1524.0, 48.666666666666629, 48.666666666666629 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-65",
					"maxclass" : "gain~",
					"multichannelvariant" : 1,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "multichannelsignal", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 657.0, 1628.0, 65.141666666666424, 18.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-337",
					"local" : 1,
					"maxclass" : "mc.ezdac~",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 657.0, 1657.0, 45.0, 45.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-358",
					"maxclass" : "meter~",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "float" ],
					"patching_rect" : [ 731.0, 1628.0, 84.583333333333371, 18.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-66",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "multichannelsignal", "", "" ],
					"patching_rect" : [ 657.0, 1593.0, 122.0, 22.0 ],
					"text" : "somax.audiorenderer",
					"varname" : "somax.audiorenderer"
				}

			}
, 			{
				"box" : 				{
					"hidden" : 1,
					"id" : "obj-47",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 848.0, 471.0, 70.0, 22.0 ],
					"text" : "loadmess 0"
				}

			}
, 			{
				"box" : 				{
					"hidden" : 1,
					"id" : "obj-58",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 6,
							"revision" : 5,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 59.0, 106.0, 640.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"assistshowspatchername" : 0,
						"boxes" : [ 							{
								"box" : 								{
									"fontname" : "Arial",
									"fontsize" : 13.0,
									"id" : "obj-6",
									"linecount" : 3,
									"maxclass" : "comment",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 137.0, 26.0, 445.0, 50.0 ],
									"text" : "For this particular maxhelp, it's unlikely that we want two players in different tabs playing simultaneously. \nFor this reason, this subpatcher will disable all players in all the other tabs",
									"textcolor" : [ 0.501960784313725, 0.501960784313725, 0.501960784313725, 1.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-10",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "int" ],
									"patching_rect" : [ 77.0, 26.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-9",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "bang", "" ],
									"patching_rect" : [ 77.0, 70.0, 34.0, 22.0 ],
									"text" : "sel 1"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-8",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 77.0, 313.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-7",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 127.0, 269.0, 29.5, 22.0 ],
									"text" : "0"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-5",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 77.0, 234.0, 69.0, 22.0 ],
									"text" : "route tab02"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-4",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 77.0, 102.0, 39.0, 22.0 ],
									"text" : "tab02"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-2",
									"maxclass" : "newobj",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 77.0, 193.0, 183.0, 22.0 ],
									"text" : "r player_maxhelp_enable_toggle"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-1",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 77.0, 139.0, 185.0, 22.0 ],
									"text" : "s player_maxhelp_enable_toggle"
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-9", 0 ],
									"source" : [ "obj-10", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-5", 0 ],
									"source" : [ "obj-2", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-1", 0 ],
									"source" : [ "obj-4", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-7", 0 ],
									"source" : [ "obj-5", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-8", 0 ],
									"source" : [ "obj-7", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-4", 0 ],
									"source" : [ "obj-9", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 646.0, 499.5, 120.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p disable_other_tabs"
				}

			}
, 			{
				"box" : 				{
					"hidden" : 1,
					"id" : "obj-62",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 629.0, 398.5, 70.0, 22.0 ],
					"text" : "loadmess 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-63",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 629.0, 446.5, 36.124999999999602, 36.124999999999602 ]
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 18.0,
					"id" : "obj-75",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 538.0, 450.062499999999773, 73.0, 29.0 ],
					"text" : "initialize"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-29",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 672.0, 581.5, 54.0, 21.0 ],
					"saved_attribute_attributes" : 					{
						"textcolor" : 						{
							"expression" : "themecolor.theme_textcolor"
						}

					}
,
					"text" : "reactive"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Arial",
					"fontsize" : 13.0,
					"id" : "obj-30",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 672.0, 565.5, 82.0, 21.0 ],
					"saved_attribute_attributes" : 					{
						"textcolor" : 						{
							"expression" : "themecolor.theme_textcolor"
						}

					}
,
					"text" : "continuous"
				}

			}
, 			{
				"box" : 				{
					"disabled" : [ 0, 0 ],
					"id" : "obj-43",
					"itemtype" : 0,
					"maxclass" : "radiogroup",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 654.0, 567.5, 18.0, 34.0 ],
					"size" : 2,
					"value" : 0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-67",
					"linecount" : 2,
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 763.0, 531.5, 121.0, 33.0 ],
					"saved_attribute_attributes" : 					{
						"textcolor" : 						{
							"expression" : "themecolor.theme_textcolor"
						}

					}
,
					"text" : "bang: trigger next (reactive mode only)",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 797.0, 567.5, 34.0, 34.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-335",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 654.0, 604.5, 55.0, 22.0 ],
					"text" : "mode $1"
				}

			}
, 			{
				"box" : 				{
					"bgmode" : 0,
					"border" : 0,
					"clickthrough" : 0,
					"enablehscroll" : 0,
					"enablevscroll" : 0,
					"id" : "obj-4",
					"lockeddragscroll" : 0,
					"lockedsize" : 0,
					"maxclass" : "bpatcher",
					"name" : "somax.server.app.maxpat",
					"numinlets" : 1,
					"numoutlets" : 4,
					"offset" : [ 0.0, 0.0 ],
					"outlettype" : [ "", "", "", "" ],
					"patching_rect" : [ 620.0, 36.0, 265.0, 306.0 ],
					"varname" : "somax.server.app",
					"viewvisibility" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 470.0, 335.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 387.0, 335.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 529.0, 135.0, 32.0, 22.0 ],
					"text" : "print"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 466.5, 386.0, 29.5, 22.0 ],
					"text" : "1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 383.0, 386.0, 29.5, 22.0 ],
					"text" : "0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "" ],
					"patching_rect" : [ 375.0, 272.0, 177.0, 22.0 ],
					"text" : "route hand-to-head raised-hand"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 375.0, 210.0, 57.0, 22.0 ],
					"text" : "unpack s"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 381.0, 99.0, 97.0, 22.0 ],
					"text" : "udpreceive 8000"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 381.0, 153.0, 113.0, 22.0 ],
					"text" : "OSC-route /gesture"
				}

			}
, 			{
				"box" : 				{
					"background" : 1,
					"bgcolor" : [ 1.0, 0.788235, 0.470588, 1.0 ],
					"hint" : "",
					"id" : "obj-86",
					"ignoreclick" : 1,
					"legacytextcolor" : 1,
					"maxclass" : "textbutton",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 708.0, 1657.0, 20.0, 20.0 ],
					"rounded" : 60.0,
					"text" : "1",
					"textcolor" : [ 0.34902, 0.34902, 0.34902, 1.0 ]
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"source" : [ "obj-16", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"source" : [ "obj-23", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-145", 0 ],
					"source" : [ "obj-25", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-66", 0 ],
					"source" : [ "obj-25", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"source" : [ "obj-335", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-335", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"hidden" : 1,
					"source" : [ "obj-47", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-63", 0 ],
					"hidden" : 1,
					"midpoints" : [ 655.5, 529.708333333333371, 619.0, 529.708333333333371, 619.0, 435.145833333333599, 638.5, 435.145833333333599 ],
					"source" : [ "obj-58", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-63", 0 ],
					"hidden" : 1,
					"source" : [ "obj-62", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"order" : 1,
					"source" : [ "obj-63", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-58", 0 ],
					"hidden" : 1,
					"order" : 0,
					"source" : [ "obj-63", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-337", 0 ],
					"source" : [ "obj-65", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-358", 0 ],
					"midpoints" : [ 666.5, 1623.5, 740.5, 1623.5 ],
					"order" : 0,
					"source" : [ "obj-66", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-65", 0 ],
					"order" : 1,
					"source" : [ "obj-66", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"order" : 0,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"order" : 1,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-25", 0 ],
					"source" : [ "obj-75", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-9", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"source" : [ "obj-9", 1 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-25::obj-118::obj-114" : [ "live.gain~[1]", "live.gain~", 0 ],
			"obj-25::obj-118::obj-119" : [ "live.text[67]", "live.text[30]", 0 ],
			"obj-25::obj-118::obj-2::obj-119" : [ "live.text[66]", "live.text[30]", 0 ],
			"obj-25::obj-118::obj-2::obj-13" : [ "live.text[28]", "live.text", 0 ],
			"obj-25::obj-118::obj-2::obj-140" : [ "mc.live.gain~[9]", "mc.live.gain~", 0 ],
			"obj-25::obj-118::obj-2::obj-62::obj-1" : [ "source[13]", "source", 0 ],
			"obj-25::obj-118::obj-42" : [ "live.toggle", "live.toggle", 0 ],
			"obj-25::obj-118::obj-55" : [ "live.gain~", "live.gain~", 0 ],
			"obj-25::obj-17::obj-103" : [ "influence delay[7]", "influencedelay", 0 ],
			"obj-25::obj-17::obj-10::obj-103" : [ "influence delay[5]", "influencedelay", 0 ],
			"obj-25::obj-17::obj-10::obj-21" : [ "onset[5]", "onset", 0 ],
			"obj-25::obj-17::obj-10::obj-26" : [ "chroma scaling factor[16]", "chroma", 0 ],
			"obj-25::obj-17::obj-10::obj-28" : [ "chromaonset[5]", "chromaonset", 0 ],
			"obj-25::obj-17::obj-10::obj-29" : [ "enable[5]", "enable", 0 ],
			"obj-25::obj-17::obj-10::obj-30" : [ "chroma scaling factor[15]", "chroma", 0 ],
			"obj-25::obj-17::obj-10::obj-46::obj-1" : [ "source[11]", "source", 0 ],
			"obj-25::obj-17::obj-10::obj-9" : [ "pitch[5]", "pitch", 0 ],
			"obj-25::obj-17::obj-2::obj-103" : [ "influence delay", "influencedelay", 0 ],
			"obj-25::obj-17::obj-2::obj-21" : [ "onset[2]", "onset", 0 ],
			"obj-25::obj-17::obj-2::obj-26" : [ "chroma scaling factor[10]", "chroma", 0 ],
			"obj-25::obj-17::obj-2::obj-28" : [ "chromaonset[2]", "chromaonset", 0 ],
			"obj-25::obj-17::obj-2::obj-29" : [ "enable[2]", "enable", 0 ],
			"obj-25::obj-17::obj-2::obj-30" : [ "chroma scaling factor[2]", "chroma", 0 ],
			"obj-25::obj-17::obj-2::obj-46::obj-1" : [ "source[5]", "source", 0 ],
			"obj-25::obj-17::obj-2::obj-9" : [ "pitch[2]", "pitch", 0 ],
			"obj-25::obj-17::obj-33::obj-103" : [ "influence delay[6]", "influencedelay", 0 ],
			"obj-25::obj-17::obj-33::obj-21" : [ "onset[6]", "onset", 0 ],
			"obj-25::obj-17::obj-33::obj-26" : [ "chroma scaling factor[17]", "chroma", 0 ],
			"obj-25::obj-17::obj-33::obj-28" : [ "chromaonset[6]", "chromaonset", 0 ],
			"obj-25::obj-17::obj-33::obj-29" : [ "enable[6]", "enable", 0 ],
			"obj-25::obj-17::obj-33::obj-30" : [ "chroma scaling factor[18]", "chroma", 0 ],
			"obj-25::obj-17::obj-33::obj-46::obj-1" : [ "source[12]", "source", 0 ],
			"obj-25::obj-17::obj-33::obj-9" : [ "pitch[6]", "pitch", 0 ],
			"obj-25::obj-17::obj-6::obj-103" : [ "influence delay[4]", "influencedelay", 0 ],
			"obj-25::obj-17::obj-6::obj-21" : [ "onset[4]", "onset", 0 ],
			"obj-25::obj-17::obj-6::obj-26" : [ "chroma scaling factor[13]", "chroma", 0 ],
			"obj-25::obj-17::obj-6::obj-28" : [ "chromaonset[4]", "chromaonset", 0 ],
			"obj-25::obj-17::obj-6::obj-29" : [ "enable[4]", "enable", 0 ],
			"obj-25::obj-17::obj-6::obj-30" : [ "chroma scaling factor[14]", "chroma", 0 ],
			"obj-25::obj-17::obj-6::obj-46::obj-1" : [ "source[7]", "source", 0 ],
			"obj-25::obj-17::obj-6::obj-9" : [ "pitch[4]", "pitch", 0 ],
			"obj-25::obj-25::obj-1" : [ "Gain", "Gain", 0 ],
			"obj-25::obj-25::obj-44" : [ "live.dial[1]", "Width", 0 ],
			"obj-25::obj-25::obj-46" : [ "live.dial", "Pan", 0 ],
			"obj-25::obj-3::obj-1115" : [ "continuity[22]", "continuity", 0 ],
			"obj-25::obj-3::obj-1150" : [ "live.text[65]", "live.text", 0 ],
			"obj-25::obj-3::obj-1179" : [ "continuity[23]", "continuity", 0 ],
			"obj-25::obj-3::obj-123::obj-1" : [ "live.text[88]", "live.text", 0 ],
			"obj-25::obj-3::obj-123::obj-2" : [ "live.text[25]", "live.text", 0 ],
			"obj-25::obj-3::obj-123::obj-3" : [ "live.text[89]", "live.text", 0 ],
			"obj-25::obj-3::obj-14::obj-12" : [ "live.slider[2]", "live.slider[2]", 0 ],
			"obj-25::obj-3::obj-14::obj-128" : [ "live.text[62]", "live.text", 1 ],
			"obj-25::obj-3::obj-14::obj-135" : [ "live.text[59]", "live.text", 1 ],
			"obj-25::obj-3::obj-14::obj-153" : [ "live.text[61]", "live.text", 1 ],
			"obj-25::obj-3::obj-14::obj-163" : [ "live.text[60]", "live.text", 1 ],
			"obj-25::obj-3::obj-14::obj-173" : [ "live.text[76]", "live.text", 1 ],
			"obj-25::obj-3::obj-14::obj-39" : [ "live.tab[1]", "live.tab", 0 ],
			"obj-25::obj-3::obj-14::obj-40" : [ "live.slider[4]", "live.slider[2]", 0 ],
			"obj-25::obj-3::obj-14::obj-64" : [ "live.text[52]", "live.text", 0 ],
			"obj-25::obj-3::obj-16::obj-26" : [ "corpusname[4]", "corpusname", 0 ],
			"obj-25::obj-3::obj-2" : [ "heldnotesmode[6]", "heldnotesmode", 0 ],
			"obj-25::obj-3::obj-32" : [ "heldnotesmode[3]", "heldnotesmode", 0 ],
			"obj-25::obj-3::obj-407::obj-1001::obj-89::obj-1" : [ "live.text[91]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-1001::obj-89::obj-2" : [ "live.text[74]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-1001::obj-89::obj-3" : [ "live.text[90]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-1039::obj-89::obj-1" : [ "live.text[38]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-1039::obj-89::obj-2" : [ "live.text[92]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-1039::obj-89::obj-3" : [ "live.text[44]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-1105" : [ "harmonincpeakdecay[8]", "harmonincpeakdecay", 0 ],
			"obj-25::obj-3::obj-407::obj-1115" : [ "continuity[1]", "continuity", 0 ],
			"obj-25::obj-3::obj-407::obj-1175" : [ "heldnotesmode[2]", "heldnotesmode", 0 ],
			"obj-25::obj-3::obj-407::obj-1179" : [ "continuity[16]", "continuity", 0 ],
			"obj-25::obj-3::obj-407::obj-12" : [ "melodicmod12[1]", "melodicmod12", 0 ],
			"obj-25::obj-3::obj-407::obj-120" : [ "melodicbypass[1]", "melodicbypass", 0 ],
			"obj-25::obj-3::obj-407::obj-1218" : [ "simultaneousonsets[2]", "artificialmidities", 0 ],
			"obj-25::obj-3::obj-407::obj-126" : [ "harmonicbypass[1]", "harmonicbypass", 0 ],
			"obj-25::obj-3::obj-407::obj-134" : [ "continuity[17]", "continuity", 0 ],
			"obj-25::obj-3::obj-407::obj-1344" : [ "enforcetaboo[4]", "enforcetaboo", 0 ],
			"obj-25::obj-3::obj-407::obj-140" : [ "resetinfluences[1]", "resetinfluences", 0 ],
			"obj-25::obj-3::obj-407::obj-144" : [ "harmonicngramorder[1]", "harmonicngramorder", 0 ],
			"obj-25::obj-3::obj-407::obj-1444" : [ "outputprobability[4]", "outputprobability", 0 ],
			"obj-25::obj-3::obj-407::obj-152" : [ "selfngramorder[1]", "selfngramorder", 0 ],
			"obj-25::obj-3::obj-407::obj-154" : [ "melodicngramorder[4]", "melodicngramorder", 0 ],
			"obj-25::obj-3::obj-407::obj-19" : [ "selfmod12[4]", "selfmod12", 0 ],
			"obj-25::obj-3::obj-407::obj-22" : [ "selfmelodicbypass[1]", "selfmelodicbypass", 0 ],
			"obj-25::obj-3::obj-407::obj-254" : [ "harmonincpeakdecay[2]", "harmonincpeakdecay", 0 ],
			"obj-25::obj-3::obj-407::obj-255" : [ "melodicpeakdecay[4]", "melodicpeakdecay", 0 ],
			"obj-25::obj-3::obj-407::obj-256" : [ "selfpeakdecay[1]", "selfpeakdecay", 0 ],
			"obj-25::obj-3::obj-407::obj-270::obj-1226" : [ "width[1]", "Width", 0 ],
			"obj-25::obj-3::obj-407::obj-270::obj-1227" : [ "center[1]", "Center", 0 ],
			"obj-25::obj-3::obj-407::obj-270::obj-1240" : [ "live.slider[3]", "live.slider", 0 ],
			"obj-25::obj-3::obj-407::obj-270::obj-1241" : [ "live.numbox[3]", "live.numbox[2]", 0 ],
			"obj-25::obj-3::obj-407::obj-270::obj-622" : [ "__exp_velocityenable[1]", "__exp_velocityenable", 0 ],
			"obj-25::obj-3::obj-407::obj-270::obj-889" : [ "weight[1]", "Weight", 0 ],
			"obj-25::obj-3::obj-407::obj-295" : [ "playingmode[4]", "playingmode", 0 ],
			"obj-25::obj-3::obj-407::obj-298" : [ "simultaneousonsets[7]", "simultaneousonsets", 0 ],
			"obj-25::obj-3::obj-407::obj-328" : [ "decaybasis[1]", "decaybasis", 0 ],
			"obj-25::obj-3::obj-407::obj-387::obj-89::obj-1" : [ "live.text[94]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-387::obj-89::obj-2" : [ "live.text[51]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-387::obj-89::obj-3" : [ "live.text[95]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-497::obj-89::obj-1" : [ "live.text[75]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-497::obj-89::obj-2" : [ "live.text[50]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-497::obj-89::obj-3" : [ "live.text[93]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-570" : [ "__exp_melodicpitchfromchords[4]", "__exp_melodicpitchfromchords", 0 ],
			"obj-25::obj-3::obj-407::obj-575" : [ "__exp_tempoconsistencysigma[4]", "__exp_tempoconsistencysigma", 0 ],
			"obj-25::obj-3::obj-407::obj-642" : [ "__exp_numnotessigma[1]", "__exp_numnotessigma", 0 ],
			"obj-25::obj-3::obj-407::obj-653" : [ "__exp_numnotesenable[4]", "__exp_numnotesenable", 0 ],
			"obj-25::obj-3::obj-407::obj-656" : [ "__exp_numnotesmu[1]", "__exp_numnotesmu", 0 ],
			"obj-25::obj-3::obj-407::obj-667" : [ "selfharmonicbypass[1]", "selfharmonicbypass", 0 ],
			"obj-25::obj-3::obj-407::obj-670" : [ "harmonicbypass[2]", "harmonicbypass", 0 ],
			"obj-25::obj-3::obj-407::obj-679" : [ "selfharmonicngramorder[1]", "selfharmonicngramorder", 0 ],
			"obj-25::obj-3::obj-407::obj-685" : [ "harmonincpeakdecay[5]", "harmonincpeakdecay[1]", 0 ],
			"obj-25::obj-3::obj-407::obj-688" : [ "__exp_durationsigma[4]", "__exp_durationsigma", 0 ],
			"obj-25::obj-3::obj-407::obj-702" : [ "__exp_durationmu[1]", "__exp_durationmu", 0 ],
			"obj-25::obj-3::obj-407::obj-722" : [ "__exp_octavebandsenable[4]", "__exp_octavebandsenable", 0 ],
			"obj-25::obj-3::obj-407::obj-733" : [ "__exp_octavebands[1]", "__exp_octavebands", 0 ],
			"obj-25::obj-3::obj-407::obj-746" : [ "__exp_selfpitchfromchords[4]", "__exp_selfpitchfromchords", 0 ],
			"obj-25::obj-3::obj-407::obj-763" : [ "__exp_autojumpforcejump[1]", "__exp_autojumpforcejump", 0 ],
			"obj-25::obj-3::obj-407::obj-774" : [ "__exp_autojumpenable[1]", "__exp_autojumpenable", 0 ],
			"obj-25::obj-3::obj-407::obj-777" : [ "__exp_autojumpactivate[1]", "__exp_autojumpactivate", 0 ],
			"obj-25::obj-3::obj-407::obj-799" : [ "__exp_tempoconsistencyenable[4]", "__exp_tempoconsistencyenable", 0 ],
			"obj-25::obj-3::obj-407::obj-802" : [ "__exp_tempoconsistencylen[4]", "__exp_tempoconsistencylen", 0 ],
			"obj-25::obj-3::obj-407::obj-814" : [ "harmonincpeakdecay[6]", "harmonincpeakdecay", 0 ],
			"obj-25::obj-3::obj-407::obj-842::obj-89::obj-1" : [ "live.text[49]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-842::obj-89::obj-2" : [ "live.text[85]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-842::obj-89::obj-3" : [ "live.text[73]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-843" : [ "harmonicngramorder[2]", "harmonicngramorder", 0 ],
			"obj-25::obj-3::obj-407::obj-860" : [ "harmonincpeakdecay[3]", "harmonincpeakdecay[1]", 0 ],
			"obj-25::obj-3::obj-407::obj-865" : [ "selfharmonicngramorder[4]", "selfharmonicngramorder", 0 ],
			"obj-25::obj-3::obj-407::obj-870" : [ "selfharmonicbypass[4]", "selfharmonicbypass", 0 ],
			"obj-25::obj-3::obj-407::obj-871" : [ "harmonincpeakdecay[7]", "harmonincpeakdecay", 0 ],
			"obj-25::obj-3::obj-407::obj-96::obj-89::obj-1" : [ "live.text[46]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-96::obj-89::obj-2" : [ "live.text[43]", "live.text", 0 ],
			"obj-25::obj-3::obj-407::obj-96::obj-89::obj-3" : [ "live.text[37]", "live.text", 0 ],
			"obj-25::obj-3::obj-79::obj-1" : [ "live.text[121]", "live.text", 0 ],
			"obj-25::obj-3::obj-79::obj-2" : [ "live.text[120]", "live.text", 0 ],
			"obj-25::obj-3::obj-79::obj-3" : [ "live.text[122]", "live.text", 0 ],
			"obj-25::obj-3::obj-85::obj-1" : [ "live.text[96]", "live.text", 0 ],
			"obj-25::obj-3::obj-85::obj-2" : [ "live.text[77]", "live.text", 0 ],
			"obj-25::obj-3::obj-85::obj-3" : [ "live.text[97]", "live.text", 0 ],
			"obj-25::obj-3::obj-87::obj-1" : [ "live.text[45]", "live.text", 0 ],
			"obj-25::obj-3::obj-87::obj-2" : [ "live.text[42]", "live.text", 0 ],
			"obj-25::obj-3::obj-87::obj-3" : [ "live.text[24]", "live.text", 0 ],
			"obj-25::obj-3::obj-89::obj-1" : [ "live.text[47]", "live.text", 0 ],
			"obj-25::obj-3::obj-89::obj-2" : [ "live.text[72]", "live.text", 0 ],
			"obj-25::obj-3::obj-89::obj-3" : [ "live.text[48]", "live.text", 0 ],
			"obj-25::obj-3::obj-91::obj-1" : [ "live.text[84]", "live.text", 0 ],
			"obj-25::obj-3::obj-91::obj-2" : [ "live.text[87]", "live.text", 0 ],
			"obj-25::obj-3::obj-91::obj-3" : [ "live.text[86]", "live.text", 0 ],
			"obj-25::obj-3::obj-94::obj-1" : [ "live.text[98]", "live.text", 0 ],
			"obj-25::obj-3::obj-94::obj-2" : [ "live.text[78]", "live.text", 0 ],
			"obj-25::obj-3::obj-94::obj-3" : [ "live.text[99]", "live.text", 0 ],
			"obj-25::obj-6::obj-98" : [ "live.text[6]", "live.text[26]", 0 ],
			"obj-26::obj-121" : [ "Gain[4]", "Gain", 0 ],
			"obj-26::obj-46" : [ "live.dial[2]", "Pan", 0 ],
			"obj-26::obj-95" : [ "Delay", "Delay", 0 ],
			"obj-4::obj-13::obj-1" : [ "source[10]", "source", 0 ],
			"obj-4::obj-2::obj-395::obj-2" : [ "live.text[5]", "live.text[4]", 0 ],
			"obj-4::obj-2::obj-395::obj-375" : [ "mc.live.gain~[8]", "click", 0 ],
			"obj-4::obj-2::obj-395::obj-441" : [ "mc.live.gain~[7]", "corpus", 0 ],
			"obj-4::obj-2::obj-395::obj-469" : [ "live.text[69]", "live.text[11]", 0 ],
			"obj-4::obj-2::obj-395::obj-472" : [ "live.text[7]", "live.text[11]", 0 ],
			"obj-4::obj-2::obj-395::obj-490" : [ "live.text[70]", "live.text[11]", 0 ],
			"obj-66::obj-98" : [ "live.text[36]", "live.text[26]", 0 ],
			"parameterbanks" : 			{
				"0" : 				{
					"index" : 0,
					"name" : "",
					"parameters" : [ "-", "-", "-", "-", "-", "-", "-", "-" ]
				}

			}
,
			"parameter_overrides" : 			{
				"obj-25::obj-118::obj-2::obj-13" : 				{
					"parameter_longname" : "live.text[28]"
				}
,
				"obj-25::obj-118::obj-2::obj-62::obj-1" : 				{
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_unitstyle" : 10
				}
,
				"obj-25::obj-17::obj-103" : 				{
					"parameter_longname" : "influence delay[7]"
				}
,
				"obj-25::obj-17::obj-10::obj-103" : 				{
					"parameter_longname" : "influence delay[5]"
				}
,
				"obj-25::obj-17::obj-10::obj-26" : 				{
					"parameter_longname" : "chroma scaling factor[16]"
				}
,
				"obj-25::obj-17::obj-10::obj-30" : 				{
					"parameter_longname" : "chroma scaling factor[15]"
				}
,
				"obj-25::obj-17::obj-10::obj-46::obj-1" : 				{
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_unitstyle" : 10
				}
,
				"obj-25::obj-17::obj-2::obj-46::obj-1" : 				{
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_unitstyle" : 10
				}
,
				"obj-25::obj-17::obj-33::obj-103" : 				{
					"parameter_longname" : "influence delay[6]"
				}
,
				"obj-25::obj-17::obj-33::obj-26" : 				{
					"parameter_longname" : "chroma scaling factor[17]"
				}
,
				"obj-25::obj-17::obj-33::obj-30" : 				{
					"parameter_longname" : "chroma scaling factor[18]"
				}
,
				"obj-25::obj-17::obj-33::obj-46::obj-1" : 				{
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_unitstyle" : 10
				}
,
				"obj-25::obj-17::obj-6::obj-103" : 				{
					"parameter_longname" : "influence delay[4]"
				}
,
				"obj-25::obj-17::obj-6::obj-26" : 				{
					"parameter_longname" : "chroma scaling factor[13]"
				}
,
				"obj-25::obj-17::obj-6::obj-30" : 				{
					"parameter_longname" : "chroma scaling factor[14]"
				}
,
				"obj-25::obj-17::obj-6::obj-46::obj-1" : 				{
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_unitstyle" : 10
				}
,
				"obj-25::obj-3::obj-123::obj-1" : 				{
					"parameter_longname" : "live.text[88]"
				}
,
				"obj-25::obj-3::obj-123::obj-2" : 				{
					"parameter_longname" : "live.text[25]"
				}
,
				"obj-25::obj-3::obj-123::obj-3" : 				{
					"parameter_longname" : "live.text[89]"
				}
,
				"obj-25::obj-3::obj-14::obj-173" : 				{
					"parameter_longname" : "live.text[76]"
				}
,
				"obj-25::obj-3::obj-16::obj-26" : 				{
					"parameter_invisible" : 1,
					"parameter_modmode" : 0,
					"parameter_unitstyle" : 10
				}
,
				"obj-25::obj-3::obj-407::obj-1001::obj-89::obj-1" : 				{
					"parameter_longname" : "live.text[91]"
				}
,
				"obj-25::obj-3::obj-407::obj-1001::obj-89::obj-2" : 				{
					"parameter_longname" : "live.text[74]"
				}
,
				"obj-25::obj-3::obj-407::obj-1001::obj-89::obj-3" : 				{
					"parameter_longname" : "live.text[90]"
				}
,
				"obj-25::obj-3::obj-407::obj-1039::obj-89::obj-1" : 				{
					"parameter_longname" : "live.text[38]"
				}
,
				"obj-25::obj-3::obj-407::obj-1039::obj-89::obj-2" : 				{
					"parameter_longname" : "live.text[92]"
				}
,
				"obj-25::obj-3::obj-407::obj-1039::obj-89::obj-3" : 				{
					"parameter_longname" : "live.text[44]"
				}
,
				"obj-25::obj-3::obj-407::obj-387::obj-89::obj-1" : 				{
					"parameter_longname" : "live.text[94]"
				}
,
				"obj-25::obj-3::obj-407::obj-387::obj-89::obj-2" : 				{
					"parameter_longname" : "live.text[51]"
				}
,
				"obj-25::obj-3::obj-407::obj-387::obj-89::obj-3" : 				{
					"parameter_longname" : "live.text[95]"
				}
,
				"obj-25::obj-3::obj-407::obj-497::obj-89::obj-1" : 				{
					"parameter_longname" : "live.text[75]"
				}
,
				"obj-25::obj-3::obj-407::obj-497::obj-89::obj-2" : 				{
					"parameter_longname" : "live.text[50]"
				}
,
				"obj-25::obj-3::obj-407::obj-497::obj-89::obj-3" : 				{
					"parameter_longname" : "live.text[93]"
				}
,
				"obj-25::obj-3::obj-407::obj-842::obj-89::obj-1" : 				{
					"parameter_longname" : "live.text[49]"
				}
,
				"obj-25::obj-3::obj-407::obj-842::obj-89::obj-2" : 				{
					"parameter_longname" : "live.text[85]"
				}
,
				"obj-25::obj-3::obj-407::obj-842::obj-89::obj-3" : 				{
					"parameter_longname" : "live.text[73]"
				}
,
				"obj-25::obj-3::obj-407::obj-96::obj-89::obj-1" : 				{
					"parameter_longname" : "live.text[46]"
				}
,
				"obj-25::obj-3::obj-407::obj-96::obj-89::obj-2" : 				{
					"parameter_longname" : "live.text[43]"
				}
,
				"obj-25::obj-3::obj-407::obj-96::obj-89::obj-3" : 				{
					"parameter_longname" : "live.text[37]"
				}
,
				"obj-25::obj-3::obj-85::obj-1" : 				{
					"parameter_longname" : "live.text[96]"
				}
,
				"obj-25::obj-3::obj-85::obj-2" : 				{
					"parameter_longname" : "live.text[77]"
				}
,
				"obj-25::obj-3::obj-85::obj-3" : 				{
					"parameter_longname" : "live.text[97]"
				}
,
				"obj-25::obj-3::obj-87::obj-1" : 				{
					"parameter_longname" : "live.text[45]"
				}
,
				"obj-25::obj-3::obj-87::obj-2" : 				{
					"parameter_longname" : "live.text[42]"
				}
,
				"obj-25::obj-3::obj-87::obj-3" : 				{
					"parameter_longname" : "live.text[24]"
				}
,
				"obj-25::obj-3::obj-89::obj-1" : 				{
					"parameter_longname" : "live.text[47]"
				}
,
				"obj-25::obj-3::obj-89::obj-2" : 				{
					"parameter_longname" : "live.text[72]"
				}
,
				"obj-25::obj-3::obj-89::obj-3" : 				{
					"parameter_longname" : "live.text[48]"
				}
,
				"obj-25::obj-3::obj-91::obj-1" : 				{
					"parameter_longname" : "live.text[84]"
				}
,
				"obj-25::obj-3::obj-91::obj-2" : 				{
					"parameter_longname" : "live.text[87]"
				}
,
				"obj-25::obj-3::obj-91::obj-3" : 				{
					"parameter_longname" : "live.text[86]"
				}
,
				"obj-25::obj-3::obj-94::obj-1" : 				{
					"parameter_longname" : "live.text[98]"
				}
,
				"obj-25::obj-3::obj-94::obj-2" : 				{
					"parameter_longname" : "live.text[78]"
				}
,
				"obj-25::obj-3::obj-94::obj-3" : 				{
					"parameter_longname" : "live.text[99]"
				}
,
				"obj-4::obj-13::obj-1" : 				{
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_unitstyle" : 10
				}
,
				"obj-4::obj-2::obj-395::obj-469" : 				{
					"parameter_longname" : "live.text[69]"
				}
,
				"obj-4::obj-2::obj-395::obj-490" : 				{
					"parameter_longname" : "live.text[70]"
				}
,
				"obj-66::obj-98" : 				{
					"parameter_longname" : "live.text[36]"
				}

			}
,
			"inherited_shortname" : 1
		}
,
		"dependency_cache" : [ 			{
				"name" : "OMax.yin+.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/influencers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/influencers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "OSC-route.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "Yin+.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/influencers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/influencers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "abstraction_path.js",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/javascript",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/javascript",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "audio2chroma.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/influencers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/influencers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "bc.autoname.js",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/javascript",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/javascript",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "bc.virfun.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "bc.yinstats.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "bonk~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "computeMemoryPitchClass.js",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/javascript",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/javascript",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "heldnotes.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "ircamdescriptor~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "kslider.compact.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "midi2chroma.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/influencers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/influencers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "midi2chroma_nofilter.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/influencers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/influencers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "midichromaanalysis.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/influencers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/influencers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "midipitchanalysis.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/influencers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/influencers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "monitor.png",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/media",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/media",
				"type" : "PNG",
				"implicit" : 1
			}
, 			{
				"name" : "omnimidiflush.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "peakmeter.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/player",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/player",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.atom.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/player",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/player",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audiocorpusbuilder.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audioinfluencer.app.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audioinfluencer.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audioinfluencer.ui.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audioinput.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audiomixer.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audiooutput.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audiorecord.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audiorecord.ui.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.audiorenderer.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.await_patcherargs.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.beatphase.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.beattracker.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.corpusbuilder.core.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.corpuspath.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.corpusview.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.descriptorview.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/player",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/player",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.filter_midichannels.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.interpreter.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.midicorpusbuilder.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.midiinfluencer.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.midiinfluencer.ui.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.midimixer.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.midioutput.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.midirenderer.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.multistatebutton.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.pan2.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.path.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.player.app.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.player.core.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.player.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.player.routerblock.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/player",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/player",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.player.routing.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/player",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/player",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.player.ui.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.print.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.receiveblock.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.regions.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.relativepath.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.routesignal.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.server.app.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.server.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.serverstatus.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/server",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/server",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.serverstatus.ui.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/server",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/server",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.source.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.uniquename.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.uniquenumber.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "somax.winresize.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "sr.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/Somax-2.7.0/patchers/resources/misc",
				"patcherrelativepath" : "../Packages/Somax-2.7.0/patchers/resources/misc",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "wfknob.png",
				"bootpath" : "C74:/media/max/picts",
				"type" : "PNG",
				"implicit" : 1
			}
, 			{
				"name" : "wfmodes.png",
				"bootpath" : "C74:/media/max/picts",
				"type" : "PNG",
				"implicit" : 1
			}
, 			{
				"name" : "yin~.mxo",
				"type" : "iLaX"
			}
 ],
		"autosave" : 0
	}

}
