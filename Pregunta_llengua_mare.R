#GRÀFICA 1

library(dplyr)
library(tidyverse)
library(tibble)

#Llegir dades
setwd("C:/Users/usuari/Documents/UAB/Visualització de Dades/PROJECTE/new_projecte/")
imm_dataset <- read.csv('./Immigracio_Emmigracio_2015-2020.csv', header = TRUE, fill=TRUE, encoding="UTF-8")

setwd("C:/Users/usuari/Documents/UAB/Visualització de Dades/PROJECTE/new_projecte/")
imm_dataset <- read.csv('./Immigracio_Emmigracio_2015-2020.csv', header = TRUE, fill=TRUE, encoding="UTF-8")
#Preparació gràfica1
group_countries1 <- imm_dataset %>%
  filter(Nacionalitat != "Espanya") %>%
  group_by(Nacionalitat) %>%
  summarize(Total=sum(Immigrants, na.rm=TRUE), Zone) %>%
  filter(Total >= 10000) %>%
  arrange(desc(Total))
#gràfica1  
ggplot(group_countries1, aes(Total, fct_reorder(Nacionalitat, Total, .desc = FALSE))) +
  geom_col(aes(fill = Zone)) +
  xlab("Nacionalitat") + ylab("Nova immigració a Barcelona als últims 6 anys") +
  geom_text(aes(label = Total), hjust = 0.001) +
  ggtitle("Països estrangers dels quals hi procedeixen més immigrants") +
  theme(
    axis.text.x=element_blank(),
    axis.ticks.x=element_blank()
  )
  
  
  #---------------------------------------------------------------
  
#Preparació gràfica2
hisp <- imm_dataset %>%
  filter(Nacionalitat != "Espanya") %>%
  filter(Zone == "Central_South_America" | Nacionalitat == "Andorra"  | Nacionalitat == "Guinea Equatorial") %>%
  summarize(Total=sum(Immigrants, na.rm=TRUE))
other <- imm_dataset %>%
  filter(Nacionalitat != "Espanya") %>%
  summarize(Total=sum(Immigrants, na.rm=TRUE)) - hisp
percentage <- round(((hisp[1,1]/(hisp[1,1]+other[1,1])) * 100),2)
#gràfica2
data <- data.frame(
  Origen=c("Països parla hispana","Altres"),
  value=c(hisp[1,1],other[1,1]),
  Perc=c(paste(as.character(percentage),"%"),paste(as.character(100-percentage),"%"))
)
# Basic piechart
ggplot(data, aes(x="", y=value, fill=Origen)) +
  geom_bar(stat="identity", width=1, color="white") +
  geom_text(aes(label = Perc),
            position = position_stack(vjust = 0.5)) +
  coord_polar("y", start=0) +
  theme_void() +
  ggtitle("Percentatges d'immigrants a BCN, de països de parla hispana/no hispana")  
