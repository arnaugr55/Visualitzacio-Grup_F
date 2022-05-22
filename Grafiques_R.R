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
