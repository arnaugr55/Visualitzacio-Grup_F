library(tidyverse)
library(dplyr)
library(ggcorrplot)
library(plotly)

####Gràfiques immigrants/emmigrants segons el gènere:####

imm_gen = read.csv('Immigracio_sexe_2015-2020.csv')
emm_gen = read.csv('Emmigracio_sexe_2015-2020.csv')


imm_gen = imm_gen[,c(1,4,5)]
emm_gen = emm_gen[,c(1,4,5)]

imm_gen_gr = imm_gen %>% group_by(Sexe, Any)%>% summarise(Immigrants=sum(Immigrants)) 
emm_gen_gr = emm_gen %>% group_by(Sexe, Any)%>% summarise(Emmigrants=sum(Emmigrants))


ggplot()+
  geom_bar(data=imm_gen_gr, aes(x=factor(Any), y=Immigrants, fill=Sexe), stat = "identity",  width = 0.8,
           position=position_dodge(width = 0.9), color='Black') + 
  xlab('Any')+ylab("Nombre d'I'mmigrants")+
  ggtitle("Evolució de la Immigració a Barcelona per Gènere") +
  theme(plot.title = element_text(hjust = 0.5))+
  labs(fill='Gènere')+
  scale_fill_brewer(palette='Dark2')

ggplot(data=emm_gen_gr, aes(x=factor(Any), y=Emmigrants, fill=Sexe))+
  geom_bar(stat = "identity",  width = 0.8,
           position=position_dodge(width = 0.9), color='Black')+
  xlab('Any')+ylab("Nombre d'I'mmigrants")+
  ggtitle("Evolució de l'Emmigració a Barcelona per Gènere") +
  theme(plot.title = element_text(hjust = 0.5))+
  labs(fill='Gènere')+
  scale_fill_brewer(palette='Dark2')
  
  
  
  ####Gràfiques ocupació mitjana i preu del lloguers:####


df_preus = read.csv('Mitjana_LLoguer_2015-2020.csv')
df_ocupacio = read.csv('Ocupacio_Mitjana_2015-2020.csv')

df_ocupacio = df_ocupacio[,c(1,2,3,6)]
names(df_ocupacio)[names(df_ocupacio) == 'Ocupacio_mitjana_.persones_.per_domicili.'] = 'Ocupacio'

df_junt = left_join(df_preus, df_ocupacio)
df_junt = df_junt%>%drop_na()


ggplot(data=df_junt, aes(x=Preu, y= Ocupacio))+geom_point()

temp = df_junt[,c(4,5)]
cormat <- round(cor(temp),2)

ggcorrplot(cormat,lab=TRUE)




fig <- df_junt %>%
  plot_ly(
    x = ~Preu,
    y = ~Ocupacio,
    frame = ~Any,
    type = 'scatter',
    mode = 'markers',
    showlegend = F
  )

fig <- fig %>%
  animation_slider(
    currentvalue = list(prefix = "ANY ", font = list(color="Blue"))
  )

fig

####GRÀFICA EXPLORATÒRIA: Riquesa de les diferents zones segons el GDP:####
setwd("C:/Users/usuari/Documents/UAB/Visualització de Dades/PROJECTE/new_projecte/")
imm_dataset <- read.csv('./GDP_zones.csv', header = TRUE, fill=TRUE, encoding="UTF-8")
group_countries2 <- imm_dataset %>% 
  filter(Nom_Barri == 'el Raval') %>%
  group_by(Zone) %>%
  summarise(mean_GDP=mean(GDP))
ggplot(group_countries2, aes(Zone, mean_GDP)) +
  geom_col(aes(fill = Zone))  +
  scale_fill_manual(values = c("darkblue", "pink", 
                               "brown", "red",
                               "darkgreen", "yellow", 
                               "purple")) +
  xlab("Zones") + ylab("GDP Mitjà dels seus països") +
  ggtitle("Riquesa de les diferents zones segons el GDP") +
  theme(
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank()
  )


  ####Gràfiques Influeix la llengua “mare” dels països dels immigrants?:####
setwd("C:/Users/usuari/Documents/UAB/Visualització de Dades/PROJECTE/new_projecte/")
imm_dataset <- read.csv('./Immigracio_Emmigracio_2015-2020.csv', header = TRUE, fill=TRUE, encoding="UTF-8")
group_countries1 <- imm_dataset %>%
  filter(Nacionalitat != "Espanya") %>%
  group_by(Nacionalitat) %>%
  summarize(Total=sum(Immigrants, na.rm=TRUE), Zone) %>%
  filter(Total >= 10000) %>%
  arrange(desc(Total))
ggplot(group_countries1, aes(Total, fct_reorder(Nacionalitat, Total, .desc = FALSE))) +
  geom_col(aes(fill = Zone)) +
  scale_fill_manual(values = c("pink", "brown", 
                               "yellow", "purple")) +
  xlab("Zones") + ylab("GDP Mitjà dels seus països") +
  xlab("Nacionalitat") + ylab("Nova immigració a Barcelona als últims 6 anys") +
  geom_text(aes(label = Total), hjust = 0.001) +
  ggtitle("Països estrangers dels quals hi procedeixen més immigrants") +
  theme(
    axis.text.x=element_blank(),
    axis.ticks.x=element_blank()
  )

hisp <- imm_dataset %>%
  filter(Nacionalitat != "Espanya") %>%
  filter(Zone == "Central South America" | Nacionalitat == "Andorra"  | Nacionalitat == "Guinea Equatorial") %>%
  summarize(Total=sum(Immigrants, na.rm=TRUE))
other <- imm_dataset %>%
  filter(Nacionalitat != "Espanya") %>%
  summarize(Total=sum(Immigrants, na.rm=TRUE)) - hisp
percentage <- round(((hisp[1,1]/(hisp[1,1]+other[1,1])) * 100),2)
data <- data.frame(
  Origen=c("Països parla hispana","Altres"),
  value=c(hisp[1,1],other[1,1]),
  Perc=c(paste(as.character(percentage),"%"),paste(as.character(100-percentage),"%"))
)
ggplot(data, aes(x="", y=value, fill=Origen)) +
  geom_bar(stat="identity", width=1, color="white") +
  geom_text(aes(label = Perc),
            position = position_stack(vjust = 0.5)) +
  coord_polar("y", start=0) +
  theme_void() +
  ggtitle("Percentatges d'immigrants a BCN, de països de parla hispana o no hispana")  
ggplot(group_countries1, aes(Total, fct_reorder(Nacionalitat, Total, .desc = FALSE))) +
  geom_col(aes(fill = Zone)) +
  xlab("Nacionalitat") + ylab("Nova immigració a Barcelona als últims 5 anys") +
  geom_text(aes(label = Total), hjust = 0.001) +
  ggtitle("Països estrangers dels quals hi procedeixen més immigrants")
